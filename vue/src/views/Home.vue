<template>
	<div class="home" style="margin-bottom:40px; margin-top: 10px;">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">Ваши словари</div>
				<div>
					<div class="button-add" v-on:click="visAdd = false" style="margin-bottom: 10px;">Создать новый словарь</div>
				</div>
			</div>
<!-- 			<ul class="list-ul">
				<li v-for="item in vocabulary" :key="item.id" class="list-item">
					<div>
						<div class="list-ul-name">{{item.name}}</div>
						<div class="list-ul-date">{{item.create_time}}</div>
					</div>
					<div class="rightpart-list">
						<div class="button-add">Тренировка</div>
						<router-link class="button-add" style="margin-left: 10px;" tag="div" 
						:to="{path: 'words/' + item.id}">Редактировать</router-link>
						<div class="button-add" style="margin-left: 10px; width: 38px; padding: 0;"
							v-bind:style="{ color: item.like ? '#376bff' : ''}"
							v-on:click="clickLike(item)">
							<font-awesome-icon icon="heart" />
						</div>
					</div>
				</li>
			</ul> -->
		</div>

		<div class="flex-boxes">
			<div v-for="item in vocabulary" :key="item.id" class="flex-box">
				<div class="right-flex-box">
					<div class="right-flex-box-item" style="margin-right: 20px;"
							v-bind:style="{ color: item.like ? '#376bff' : ''}"
							v-on:click="clickLike(item)">
							<font-awesome-icon icon="heart" size="lg"/>
					</div>
					<router-link class="right-flex-box-item" tag="div"
					:to="{path: 'words/' + item.id}"><font-awesome-icon icon="align-justify" size="lg"/></router-link>
				</div>
				<div class="left-flex-box">
					<div style="color: #9a9898; font-weight: 600; font-size: 14px; letter-spacing: 0.01px;">{{item.create_time}}</div>
				</div>
				<div class="flex-box-name">
					<div class="logo-vocab">
						<div class="logo-ul-name">{{item.name}}</div>
						<div class="logo-ul-vocab">{{item.ammount}} из 400 слов</div>
					</div>
				</div>
				<div class="flex-box-buttons">
					<div class="button-add" style="margin-bottom: 15px;">Начать тренировку</div>
					<div class="button-add" style="margin-bottom: 15px;">Добавить слово или словосочетание</div>
					
					
				</div>
			</div>
		</div>

		<div class="back-modal" v-if="!visAdd"></div>
		<div class="mat-modal" v-if="!visAdd">
			<div class="modal-title">
				Добавить Словарь
			</div>
			<form @submit.prevent="addVocabulary" class="modal-form">
				<input type="text" v-model="vocab.name" placeholder="Наименование словаря">
				<div class="modal-form-btns">
					<button class="btn-cancel" v-on:click="visAdd = true">Назад</button>
					<button class="btn-submit" type="submit" style="margin-left: 10px;">Добавить</button>
				</div>
			</form>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHeart } from '@fortawesome/free-solid-svg-icons'
import { faBook } from '@fortawesome/free-solid-svg-icons'
import { faAlignJustify } from '@fortawesome/free-solid-svg-icons'
import RPService from '../services/rps';
library.add(faHeart)
library.add(faAlignJustify)
library.add(faBook)
const rps = new RPService();

export default Vue.extend({
	name: 'Home',
	components: {
	},
	data() {
		return {
			visAdd: Boolean,
			vocabulary: null,
			vocab: {
				'name': null
			}
		};
	},
	created() {
		rps.getVocabulary().then(res => {
			this.vocabulary = res.data.vocabulary;
		});
	},
	methods: {
		addVocabulary() {
			if (this.vocab.name.trim()){
				rps.createVocabulary(this.vocab).then(() => {
					rps.getVocabulary().then(res => {
						this.vocabulary = res.data.vocabulary;
						this.visAdd = true;
						this.vocab.name = null;
					});
				});
			}
		},
		clickLike(item){
			item.like = !item.like;
			rps.editVocabulary(item).then(() => {
				rps.getVocabulary().then(res => {
					this.vocabulary = res.data.vocabulary;
				});
			});
		}
	}
});
</script>