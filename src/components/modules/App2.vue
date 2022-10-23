// yarn serve
// https://teratail.com/questions/138568

<template>
    <myHeader />

    <div  v-if="this.data==1">
      <li id="a">
        <h2>{{this.year}} 第{{this.info[this.count].name}}問</h2><br>
        <span v-html="this.info[this.count].q"></span><br><br>
        <div v-if="this.info[this.count].table==1">
          <table id="center" border="1">
            <thread>
            <tr>
              <th>選択肢</th>
              <th>(ア)</th>
              <th>(イ)</th>
              <th>(ウ)</th>
              <th>(エ)</th>
            </tr>
            </thread>
            <div v-for="j in 5" :key='j'>
              <tr>
                <th>({{this.info[this.count].options[j-1].name}})</th>
                <th>{{this.info[this.count].options[j-1].a}} </th>
                <th>{{this.info[this.count].options[j-1].i}} </th>
                <th>{{this.info[this.count].options[j-1].u}} </th>
                <th>{{this.info[this.count].options[j-1].e}} </th>
              </tr>
            </div>
          </table>
        </div>

        <div v-if="this.info[this.count].table==0">
            <div v-for="j in 5" :key='j'>
                <p>({{this.info[this.count].options[j-1].name}}): {{this.info[this.count].options[j-1].option}} </p>
            </div>
        </div>
        <div id="center">
            <a v-for="j in 5" :key='j'>
              <button height="50" width="50" @click="check(j)">({{j}})</button>
            </a>
        </div>
        <br>
        <br>
        <br>
        <div v-if="this.ans==1">
          正解：{{this.info[this.count].answer}}<br>
          {{this.info[this.count].detail}}
        </div>
      </li>
      <button height="50" width="50" v-on:click="minus_count">前の問題へ</button>
      <button v-on:click="plus_count">次の問題へ</button>
    </div>
    <p></p>
    <p></p>
    <p></p>
    <div id="a">
      <button v-on:click="getdata(2020)">2020</button>
      <button v-on:click="getdata(2021)">2021</button>
      <p></p>
      <router-link to="/">ホームへ戻る</router-link>
  </div>
  <myFooter />
</template>

<script>
import myHeader from './myHeader.vue'
import myFooter from './myFooter.vue'

export default {
  name: 'App',
  components: {
    myHeader,
    myFooter
  },
  data: function () {
    return {
      year: null, // the year of question
      info: null, // the question data
      count: 0, // number of questions from first to now
      data: 0, // flag that program gets question data
      ans: 0 // flag that program display answer
    }
  },

  methods: {
    scrollTop: function () {
      window.scrollTo({
        top: 0
        // behavior: "smooth"
      })
    },
    minus_count: function () {
      this.count--
      this.ans = 0
      this.scrollTop()
    },
    plus_count: function () {
      this.count++
      this.ans = 0
      this.scrollTop()
    },
    getdata: function (value) {
      this.year = value
      this.count = 0
      // var path = require('path');
      // // var url='./assets/db/'+this.year+'.json';
      // this.info=require(path.join('./assets/db/',this.year,'.json'))
      // this.info=require(path.join('./assets/db/2021.json'))
      if (value === 2021) {
        this.info = require('./../../assets/db/2021.json')
      }
      if (value === 2020) {
        this.info = require('./../../assets/db/2020.json')
      }
      this.data = 1
    },
    check: function (value) {
      console.log(value)
      if (value === this.info[this.count].answer) {
        alert('正解')
      } else {
        alert('不正解')
      }
      this.ans = 1
    },
    confirm () {
      return window.confirm('ページを離脱してもよろしいですか？')
    }
  },
  // mounted: function () {
  //   console.log(this.$route.params)
  //   this.year=this.$route.params

  //   if (this.year === 2021) {
  //     this.info=require('./../../assets/db/2021.json')
  //   }
  //   if (this.year === 2020) {
  //     this.info=require('./../../assets/db/2020.json')
  //   }
  //   this.data=1
  //   this.count=0
  // },

  beforeRouteLeave (to, from, next) {
    if (this.confirm() === false) return
    next()
  }
}
</script>
<style>
#a {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size:15px;
  margin-left: 100px;
  margin-right: 100px;
  color: #2c3e50;
  margin-top: 10px;
  align:"center";

}
#span{
    margin-left: 200px;
  margin-right: 200px;
}
#table1{
  margin: auto;
  width: auto;
  align:center;
}
button{
  height:5em;
  width:10em;
}
th {
  width:300px;
  align:"center";
}
#center {
  align:"center";
  margin: auto;
}
</style>
