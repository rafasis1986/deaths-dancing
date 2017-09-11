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
              <div class="input-group">
                <date-picker :config="configs.timePicker" v-model="form.time" :wrap="true"
                             placeholder="Select booking time"></date-picker>
                <div class="input-group-addon">
                  <span class="glyphicon glyphicon-time"></span>
                </div>
              </div>
            </div>
            <div v-if="enabled" class="col-md-2 col-md-offset-4">
              <button type="button" class="btn btn-primary">
                Book <span class="glyphicon glyphicon-ok-circle"></span>
              </button>
            </div>
          </div>
          <div class="col-md-12">
            <hr/>
            <vue-event-calendar :events="cEvents" @day-changed="handleDayChanged"
              @month-changed="handleMonthChanged">
                <div v-if="!seen">
                  <template scope="props">
                    <div v-for="(event, index) in cEvents" class="event-item">
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
// import ApiService from '../api/ApiService'
// import axios from 'axios'
import { API } from '../api/ApiService'

// const api = new ApiService()
const moment = require('moment')

export default {
  name: 'schedule',
  props: ['authenticated', 'showEvents'],
  data () {
    return {
      form: {
        date: new Date(),
        time: null
      },
      configs: {
        basic: {
          format: 'DD/MM/YYYY',
          useCurrent: true
        },
        timePicker: {
          format: 'HH:mm',
          useCurrent: false
        }
      },
      cEvents: [],
      seen: false,
      enabled: false,
      asyncevent: false,
      testValue: null
    }
  },
  methods: {
    handleDayChanged (data) {
      let aux = jQuery('h2.date')[0]
      if (data.events.length > 0) {
        this.seen = true
      } else {
        this.seen = false
      }
      if (aux) {
        let auxDate = new Date(data.date)
        aux.innerHTML = moment(auxDate).format('DD/MM/YYYY')
        if (auxDate.getDay() !== 0 && auxDate.getDay() !== 6) {
          this.enabled = true
        } else {
          this.enabled = false
        }
      }
      console.log('date-changed', data)
    },
    handleMonthChanged (data) {
      let aux = jQuery('h2.date')[0]
      this.seen = false
      this.enabled = false
      if (aux) {
        aux.innerHTML = 'Month: ' + data
      }
      console.log('month-changed', data)
      let auxDate = data.split('/')
      let firstMonthDay = new Date(auxDate[1], auxDate[0] - 1, 1)
      console.log(firstMonthDay)
      this.cEvents = [
        {
          date: '2017/10/02',
          title: '10 test',
          desc: 'description test'
        }]
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
    API.get('schedule/bookings/')
      .then((response) => {
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
            date: moment(data.attributes.time).format('YYYY/MM/DD'),
            title: moment(data.attributes.time).format('h:mm a'),
            desc: getBookingClient._v
          }
          return event
        })
        this.cEvents = result
      })
      .catch((e) => {
        console.log('error!!!!')
        console.log(e)
      })
  }
}
</script>
