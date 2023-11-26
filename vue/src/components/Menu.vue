<template>
	<div>
    <div class="float-menu">
      <div class="menu">
        <router-link tag="div" class="logo hover-mobile" :to="{path: '/'}">
          <span class="logo-1">Lingua</span><span class="logo-2">Trash</span>
        </router-link>

        <router-link tag="div" class="logo hover-pc" :to="{path: '/'}">
          <span class="logo-1">L</span><span class="logo-2">T</span>
        </router-link>

        <div class="menu-items">
          <div class="menu-line">
          </div>
      <!-- 		<router-link tag="div" class="menu-item" :to="{path: '/home'}">
            <font-awesome-icon icon="user-circle" size="lg" :style="{ color: '#3687e3' }"/><span>Моя страница</span>
          </router-link> -->
          <router-link tag="div" class="menu-item" :to="{path: '/'}">
            <span class="menu-item-font"><font-awesome-icon icon="book" size="lg" :style="{ color: '#3687e3' }" /></span><span class="menu-name" style="margin-left: 10px;">Словари</span>
          </router-link>

          <div class="menu-line">
          </div>
          <router-link tag="div" class="menu-item" :to="{path: '/feedback'}">
            <span class="menu-item-font"><font-awesome-icon icon="comment" size="lg" :style="{ color: '#3687e3' }"/></span><span class="menu-name" style="margin-left: 10px;">Фидбэк</span>
          </router-link>
          <router-link tag="div" class="menu-item" :to="{path: '/info'}">
            <span class="menu-item-font"><font-awesome-icon icon="question-circle" size="lg" :style="{ color: '#3687e3' }"/></span><span class="menu-name" style="margin-left: 10px;">Инфо</span>
          </router-link>
          <div class="menu-line">
          </div>
          <div class="menu-item"  v-on:click="logOut()" v-if="partner">
            <div tag="div" class="menu-item">
              <span class="menu-item-font">
                <font-awesome-icon icon="user-circle" size="lg" :style="{ color: '#3687e3' }"/>
              </span>
              <span class="menu-name" style="margin-left: 10px;">Выйти</span>
            </div>
          </div>
          <div class="menu-item"  v-on:click="visibilityLogin=false" v-if="!partner">
            <div tag="div" class="menu-item">
              <span class="menu-item-font">
                <font-awesome-icon icon="user-circle" size="lg" :style="{ color: '#3687e3' }"/>
              </span>
              <span class="menu-name" style="margin-left: 10px;">Войти</span>
            </div>
          </div>
        </div>

        <div class="calendar" v-if="calendar">
          <div class="calendar-date">
            Праздники - {{calendar.now}}
          </div>
          <ul class="holidays">
            <li v-for="item in calendar.holidays" :key="item.id">
              <div class="menu-line">
              </div>
              {{item.description}}
            </li>
          </ul>
        </div>
      </div>
    </div>
    <LogIn v-if="!visibilityLogin" @close="visibilityLogin = true" />
	</div>
</template>

<script>
import Vue from 'vue';
import LogIn from '@/components/Login';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faQuestionCircle, faUserCircle, faBook, faComment } from '@fortawesome/free-solid-svg-icons'
import RPService from '@/services/rps';
const rps = new RPService();

library.add(faUserCircle)
library.add(faBook)
library.add(faComment)
library.add(faQuestionCircle)


export default Vue.extend({
	name: 'Menu',
  components: {
		LogIn,
	},
	props: {
	},
	data() {
		return {
			partner: Boolean,
			calendar: null,
      visibilityLogin: Boolean,
		}
	},
	created() {
		rps.getMe().then((res) => {
			this.partner = res;
		});
		rps.getHolidays().then((res) => {
			this.calendar = res;
		});
	},
	methods: {
		logOut(){
			rps.logOut().then(() => {
				window.location.reload(true);
			});
		}
	}
});
</script>
