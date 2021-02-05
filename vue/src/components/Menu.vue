<template>
	<div class="float-menu">
		<div class="menu">
			<router-link tag="div" class="logo" :to="{path: '/'}">
				<span class="logo-1">Lingua</span><span class="logo-2">Trash</span>
			</router-link>

			<div class="menu-items">
				<div class="menu-line">
				</div>
		<!-- 		<router-link tag="div" class="menu-item" :to="{path: '/home'}">
					<font-awesome-icon icon="user-circle" size="lg" :style="{ color: '#3687e3' }"/><span>Моя страница</span>
				</router-link> -->
				<router-link tag="div" class="menu-item" :to="{path: '/'}">
					<span class="menu-item-font"><font-awesome-icon icon="book" size="lg" :style="{ color: '#3687e3' }" /></span><span style="margin-left: 5px;">Словари</span>
				</router-link>

				<div class="menu-line">
				</div>
				<div class="menu-item">
					<span class="menu-item-font"><font-awesome-icon icon="comment" size="lg" :style="{ color: '#3687e3' }"/></span><span style="margin-left: 5px;">Обратная связь</span>
				</div>
				<div class="menu-item">
					<span class="menu-item-font"><font-awesome-icon icon="question-circle" size="lg" :style="{ color: '#3687e3' }"/></span><span style="margin-left: 5px;">Инфо</span>
				</div>
				<div class="menu-line">
				</div>
				<div class="menu-item">
					<div tag="div" class="menu-item">
						<span class="menu-item-font"><font-awesome-icon icon="user-circle" size="lg" :style="{ color: '#3687e3' }"/></span><span style="margin-left: 5px;">Аккаунт</span>
					</div>
					
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserCircle } from '@fortawesome/free-solid-svg-icons'
import { faBook } from '@fortawesome/free-solid-svg-icons'
import { faComment } from '@fortawesome/free-solid-svg-icons'
import { faQuestionCircle } from '@fortawesome/free-solid-svg-icons'
import RPService from '../services/rps';
const rps = new RPService();

library.add(faUserCircle)
library.add(faBook)
library.add(faComment)
library.add(faQuestionCircle)



export default Vue.extend({
	name: 'Menu',
	props: {
	},
	data() {
		return {
			partner: Boolean,
		}
	},
	created() {
		rps.getMeOnly().then((res) => {
			this.partner = res.data.partner;
		});
	}
});
</script>
