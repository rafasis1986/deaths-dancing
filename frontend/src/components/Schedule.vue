<template>
  <section class="container">
    <div v-if="authenticated" class="panel panel-default profile-area">
      <div class="panel-heading header-center">
        <h3>Schedule</h3>
      </div>
      <div class="panel-body">
        <div class="row">
          <div class="col-md-6 col-md-offset-3">
            <div class="form-group">
              <label>Select booking time</label>
              <div class="input-group">
                <date-picker :config="configs.timePicker" v-model="form.time" :wrap="true"
                             placeholder="Time" ></date-picker>
                <div class="input-group-addon">
                  <span class="glyphicon glyphicon-time"></span>
                </div>
              </div>
            </div>
            <hr/>
          </div>
          <div class="col-md-12">
            <vue-event-calendar :events="cEvents" @day-changed="handleDayChanged"
              @month-changed="handleMonthChanged">
                <div v-if="!seen">
                  <template scope="props">
                    <div v-for="(event, index) in props.showEvents" class="event-item">
                      {{event}}
                    </div>
                  </template>
                </div>
            </vue-event-calendar>
          </div>
        </div>
      </div>
    </div>
    <h4 v-if="!authenticated">
      You are not logged in! Please <a @click="auth.login()">Log In</a> to continue.
    </h4>
  </section>
</template>

<script>
import jQuery from 'jquery'
const moment = require('moment')

let today = new Date()
let demoEvents = [
  {
    date: `${today.getFullYear()}/${today.getMonth() + 1}/15`,
    title: '12:00',
    desc: 'dancing with Test'
  }, {
    date: `${today.getFullYear()}/${today.getMonth() + 1}/15`,
    title: '13:00',
    desc: 'dancing with test 2'
  }, {
    date: `${today.getFullYear()}/${today.getMonth() + 2}/15`,
    title: '16:00',
    desc: 'dancing with other guy'
  }, {
    date: `${today.getFullYear()}/${today.getMonth() + 1}/05`,
    title: '09:00',
    desc: 'dancing'
  }
]

export default {
  name: 'schedule',
  props: ['authenticated'],
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
      cEvents: demoEvents,
      seen: false
    }
  },
  methods: {
    handleDayChanged (data) {
      if (data.events.length > 0) {
        this.seen = true
      } else {
        this.seen = false
      }
      var aux = jQuery('h2.date')[0]
      if (aux) {
        var auxDate = new Date(data.date)
        aux.innerHTML = moment(auxDate).format('DD/MM/YYYY')
      }
      console.log('date-changed', data)
    },
    handleMonthChanged (data) {
      this.seen = false
      var aux = jQuery('h2.date')[0]
      if (aux) {
        aux.innerHTML = 'Month: ' + data
      }
      console.log('month-changed', data)
    }
  },
  mounted () {
    var aux = jQuery('div.title')[0]
    var aux2 = jQuery('h2.date')[0]
    if (aux && aux2) {
      aux2.innerHTML = 'Month: ' + aux.innerHTML
    }
    console.log(aux)
  }
}
</script>
