<template>
	<div class="home" style="margin-bottom:40px; margin-top: 10px;" v-if="partner">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">{{partner.user}}</div>
				<div>
					<div class="button-add" v-on:click="logOut()" style="margin-bottom: 10px;">Выйти</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../services/rps';
import router from  '../router/index.ts'
const rps = new RPService();

export default Vue.extend({
	name: 'Account',
	components: {
	},
	data() {
		return {
			partner: Boolean,
		};
	},
	created() {
		rps.getMe().then((res) => {
			this.partner = res.data.partner;
		});
	},
	methods: {
		logOut(){
			rps.logOut().then(() => {
				window.location.replace("http://localhost:8080/login");
				// router.push({ name: 'login'});
			});
		}
	}
});
</script>
