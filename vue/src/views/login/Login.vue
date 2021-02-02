<template>
	<div>
		<div class="modal-form" v-if="visLogin">
			<input type="text" v-model="user.username" placeholder="Почта">
			<input type="text" v-model="user.password" placeholder="Пароль">
			<div class="modal-form-btns">
				<button class="btn-submit" style="margin-left: 10px;" v-on:click="login()">Войти</button>
				<button class="btn-submit" style="margin-left: 10px;" v-on:click="visLogin=!visLogin">Регистрация</button>
			</div>
		</div>

		<form @submit.prevent="signup" class="modal-form" v-if="!visLogin">
			<input type="text" v-model="user.username" placeholder="Почта">
			<input type="text" v-model="user.password" placeholder="Пароль">
			<div class="modal-form-btns">
				<button class="btn-submit" style="margin-left: 10px;" type="submit">Регистрация</button>
			</div>
		</form>
	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../../services/rps';
import router from  '../../router/index.ts'
const rps = new RPService();

export default Vue.extend({
	name: 'LogIn',
	components: {
	},
	data() {
		return {
			visLogin: Boolean,
			user: {
				'username': null,
				'password': null
			}
		};
	},
	methods: {
		login(){
			rps.logIn(this.user.username, this.user.password).then(res => {
				window.location.replace("http://localhost:8080/");
			});
		},
		signup(){
			rps.signUp(this.user.username, this.user.password).then(res => {
				return;
			});
		}
	}
});
</script>