<template>
	<div class="login-align">
		<div class="login-center" v-bind:class="{'reg-log': !registration}">
			<form @submit.prevent="login" class="modal-form" v-if="registration">
				<div class="login-logo">
					<span class="logo-1">Lingua</span><span class="logo-2">Trash</span>
				</div>
				<div class="login-text-css">Комфортное обучение</div>
				<input type="email " v-model="user.username" placeholder="Почта">
				<input type="password" v-model="user.password" placeholder="Пароль">
				<div class="login-text-error">
					<span v-if="error">{{error}}</span>
				</div>
				<div class="modal-form-btns">
					<button class="button-add" type="submit" style="width: 100%; margin-top: 0; height: 40px;">Войти</button>
					<div class="button-add" v-on:click="back()" style="height: 38px"><span style="font-weight: 400; margin-right: 3px;">Нет аккаунта?</span> Создайте его</div>
				</div>
			</form>

			<form @submit.prevent="signup" class="modal-form" v-if="!registration"
				style="width: 100%;">
				<div class="login-logo">
					<span class="logo-1">Lingua</span><span class="logo-2">Trash</span>
				</div>
				<div class="login-text-css">Комфортное обучение</div>
				<input type="email " v-model="user.username" placeholder="Почта">
				<input type="password" v-model="user.password" placeholder="Пароль">
				<input type="password" v-model="user.password2" placeholder="Повторный пароль">
				<div class="login-text-error">
					<span v-for="error in errorPassword" :key="error" >{{error}}</span>
					<span v-for="error in errorEmail" :key="error" >{{error}}</span>
				</div>
				<div class="modal-form-btns">
					<button class="button-add" type="submit" style="width: 100%; margin-top: 0; height: 40px;">Создать аккаунт и войти</button>
					<div class="button-add" v-on:click="back()" style="height: 38px">Назад</div>
				</div>
			</form>

			<div class="login-text" v-if="registration">
				<div class="login-text-style">
					<span>Добро пожаловать!</span> <br>
					Вы случайно наткнулись на платформу для запоминания иностранных слов <br><br>
					Для доступа к платформе нужно только "Войти"
				</div>
			</div>
		</div>
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
			registration: Boolean,
			user: {
				'username': null,
				'password': null,
				'password2': null
			},
			error: undefined,
			errorEmail: [],
			errorPassword: [],
		};
	},
	methods: {
		back(){
			this.user.username = null;
			this.user.password = null;
			this.user.password2 = null;
			this.error = undefined;
			this.errorEmail = [];
			this.errorPassword = [];
			this.registration=!this.registration;
		},
		login(){
			rps.logIn(this.user.username, this.user.password).then(res => {
				window.location.reload(true);
			}).catch( error => {
				if (error.response) {
					if (error.response.data && error.response.data.detail){
						this.error = error.response.data.detail;
					}
				} else if (error.request) {
					console.log(error.request);
				} else {
					console.log('Error', error.message);
				}
			});
		},
		signup(){
			if (this.user.password == this.user.password2){
				rps.signUp(this.user.username, this.user.password).then(res => {
					this.errorEmail = [];
					this.errorPassword = [];
					rps.logIn(this.user.username, this.user.password).then(res => {
						window.location.reload(true);
					});
				}).catch( error => {
					if (error.response) {
						if (error.response.data && error.response.data.email){
							this.errorPassword = [];
							this.errorEmail = error.response.data.email;
						}
						if (error.response.data && error.response.data.password){
							this.errorEmail = [];
							this.errorPassword = error.response.data.password;
						}
					} else if (error.request) {
						console.log(error.request);
					} else {
						console.log('Error', error.message);
					}
				});
			} else {
				this.error = ['Пароли должны совпадать'];
			}
		}
	}
});
</script>
