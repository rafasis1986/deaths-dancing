<template>
  <section class="container">
    <div v-if="authenticated" class="panel panel-default profile-area">
      <div class="panel-heading header-center">
        <h3 class="text-center">Schedule</h3>
      </div>
      <div v-if="!asyncevent" class="panel-body">
        <div class="row">
          <div class="col-md-10 col-md-offset-1">
            <div class="form-group col-md-6">
              <multiselect v-model="hourSelected" :options="options"></multiselect>
            </div>
            <div v-if="enabled" class="col-md-2 col-md-offset-4">
              <button type="button" class="btn btn-primary" v-on:click="submitBookDate">
                Book <span class="glyphicon glyphicon-ok-circle"></span>
              </button>
            </div>
          </div>
          <div class="col-md-12">
            <hr/>
            <vue-event-calendar :events="currentEvents" @day-changed="handleDayChanged"
              @month-changed="handleMonthChanged">
                <div v-if="!seen">
                  <template scope="props">
                    <div v-for="(event, index) in currentEvents" class="event-item">
                      {{event}}
                    </div>
                  </template>
                </div>
            </vue-event-calendar>
          </div>
        </div>
      </div>
      <div v-if="asyncevent" class="col-md-12 text-center">
        <img src="../assets/img/loading.svg" alt="loading"/>
      </div>
    </div>
    <h4 v-if="!authenticated">
      You are not logged in! Please <a @click="auth.login()">Log In</a> to continue.
    </h4>
  </section>
</template>

<script>
import jQuery from 'jquery'
import axios from 'axios'
import Multiselect from 'vue-multiselect'

const BASE_API_URL = 'http://localhost:8000/v1/'
const moment = require('moment')
const API = axios.create({
  baseURL: BASE_API_URL,
  headers: {
    'Authorization': localStorage.getItem('access_token'),
    'Content-Type': 'application/vnd.api+json'
  }
})

export default {
  name: 'schedule',
  props: ['authenticated', 'showEvents'],
  components: { Multiselect },
  data () {
    return {
      hourSelected: null,
      options: [],
      currentEvents: [],
      seen: false,
      enabled: false,
      asyncevent: false
    }
  },
  methods: {
    submitBookDate () {
      let aux = jQuery('h2.date')[0]
      if (aux) {
        let body = {
          'data': {
            'type': 'booking',
            'attributes': {
              'date': moment(aux.innerHTML, 'DD/MM/YYYY').format('YYYY-MM-DD'),
              'hour': this.hourSelected
            }
          }
        }
        API.post('schedule/bookings/', body)
          .then((response) => {
            this.options = []
          })
          .catch((e) => {
            console.log('error!')
            console.log(e)
          })
      }
    },
    handleDayChanged (data) {
      let aux = jQuery('h2.date')[0]
      let now = new Date()
      if (data.events.length > 0) {
        this.seen = true
      } else {
        this.seen = false
      }
      if (aux) {
        let auxDate = new Date(data.date)
        aux.innerHTML = moment(auxDate).format('DD/MM/YYYY')
        if (auxDate < now) {
          this.enabled = false
        } else if (auxDate.getDay() === 0 || auxDate.getDay() === 6) {
          this.enabled = false
        } else {
          this.enabled = true
        }
        if (this.enabled) {
          API.get('avaliable/hours/?date=' + moment(auxDate).format('DD/MM/YYYY'))
            .then((response) => {
              this.options = response.data.data.availability
            })
        } else {
          this.options = []
        }
      }
    },
    handleMonthChanged (data) {
      this.asyncevent = true
      let aux = jQuery('h2.date')[0]
      this.seen = false
      this.enabled = false
      if (aux) {
        aux.innerHTML = 'Month: ' + data
      }
      let auxDate = data.split('/')
      let dateFrom = moment(new Date(auxDate[1], auxDate[0] - 1, 1)).format('YYYY-MM-DD')
      let dateTo = moment(new Date(auxDate[1], auxDate[0], 1)).format('YYYY-MM-DD')
      API.get('schedule/bookings/?date_gt=' + dateFrom + '&date_lt=' + dateTo)
        .then((response) => {
          this.responseData = response.data
          let result = response.data.data.map((data) => {
            let getBookingClient = new Promise((resolve, reject) => {
              let iterClients = response.data.included[Symbol.iterator]()
              let current = iterClients.next()
              while (current.value) {
                if (current.value.id === data.relationships.client.data.id) {
                  resolve(current.value.attributes.email)
                }
                current = iterClients.next()
              }
            })
            let event = {
              date: moment(data.attributes.date).format('YYYY/MM/DD'),
              title: data.attributes.hour + ':00',
              desc: getBookingClient._v
            }
            return event
          })
          this.responseData = null
          this.currentEvents = result
        })
        .catch((e) => {
          console.log('error!')
          console.log(e)
        })
      this.asyncevent = false
    }
  },
  mounted () {
    let aux = jQuery('div.title')[0]
    let aux2 = jQuery('h2.date')[0]
    if (aux && aux2) {
      aux2.innerHTML = 'Month: ' + aux.innerHTML
    }
  },
  created () {
    let today = new Date()
    let currentYear = today.getFullYear()
    let currentMonth = today.getMonth()
    let dateFrom = moment(new Date(currentYear, currentMonth, 1)).format('YYYY-MM-DD')
    let dateTo = moment(new Date(currentYear, currentMonth + 1, 1)).format('YYYY-MM-DD')
    API.get('schedule/bookings/?date_gt=' + dateFrom + '&date_lt=' + dateTo)
      .then((response) => {
        this.responseData = response.data
        let result = response.data.data.map((data) => {
          let getBookingClient = new Promise((resolve, reject) => {
            let iterClients = response.data.included[Symbol.iterator]()
            let current = iterClients.next()
            while (current.value) {
              if (current.value.id === data.relationships.client.data.id) {
                resolve(current.value.attributes.email)
              }
              current = iterClients.next()
            }
          })
          let event = {
            date: moment(data.attributes.date).format('YYYY/MM/DD'),
            title: data.attributes.hour + ':00',
            desc: getBookingClient._v
          }
          return event
        })
        this.responseData = null
        this.currentEvents = result
        this.asyncevent = false
      })
      .catch((e) => {
        console.log('error!')
        console.log(e)
      })
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
