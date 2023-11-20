<template>
	<div class="home" style="margin-bottom:60px; margin-top: 10px;">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">Мои словари</div>
				<div>
					<div class="button-add" v-on:click="visAdd = false"><font-awesome-icon icon="plus" style="margin-right: 5px;"/>Cловарь</div>
				</div>
			</div>
		</div>

		<div class="loader" v-if="!vocabulary"></div>

		<div class="row-home" v-if="vocabulary">
			<div class="flex-boxes" v-if="boxes">
				<div class="flex-boxes-in scroll">
					<div v-for="item in vocabulary" :key="item.id" class="flex-box"
						v-on:mouseover="vocabularyActive=item">
						<div class="right-flex-box">
							<router-link class="right-flex-box-item" tag="div"
							:to="{path: 'words/' + item.id}" style="margin-right: 20px;">
								<font-awesome-icon icon="bars" size="lg"/>
							</router-link>
							<div class="right-flex-box-item"
									v-bind:style="{ color: item.like ? '#376bff' : ''}"
									v-on:click="clickLike(item)">
									<font-awesome-icon icon="heart" size="lg"/>
							</div>
						</div>
						<div class="left-flex-box">
							<div style="color: #9a9898; font-weight: 600; font-size: 14px; letter-spacing: 0.01px;">{{item.create_time}}</div>
						</div>
						<div class="flex-box-name">
							<div class="logo-vocab">
								<div class="logo-ul-name">{{item.name}}</div>
								<div class="logo-ul-vocab">{{item.words.length}} из 400 слов</div>
							</div>
						</div>
						<div class="flex-box-buttons">
							<div class="button-add" style="margin-bottom: 15px;" v-on:click="train(item)">Начать тренировку</div>
						</div>
					</div>

					<div class="flex-box add-vocab-box"
						v-on:mouseover="hover=false"
						v-on:mouseleave="hover=true" v-on:click="visAdd = false">
						<div  style="background: #e6e6e6; position: absolute; width: 100%; height: 100%; transition: 0.5s"
						v-bind:style="{ opacity: !hover ? '0.0' : '0.5'}"></div>

						<font-awesome-icon style="margin-right: 20px; width: 50px;" icon="plus" size="6x"
							class="add-vocab-box-mobile" />

						<div v-if="!vocabulary || vocabulary.length == 0">Создать первый словарь</div>
					</div>
				</div>
			</div>

			<div class="mat-div" v-if="vocabularyActive && width>=768" style="flex: 1; margin: 0; margin-left: 10px; padding-bottom: 5px;">
				<div class="mat-title" style="padding-bottom: 20px;">
					<div class="mat-name" style="margin-bottom: 0;">{{vocabularyActive.name}}</div>
					<div style="display: flex;">

						<div class="button-add" v-on:click="visDeleteVocab = false">
							<font-awesome-icon icon="trash" />
						</div>
					</div>
				</div>
				<ul class="list-ul list-item-over scroll" v-bind:style="{ 'max-height': vocabulary.length==1 ? '340px' : '450px'}">

					<div class="list-item add-vocab-box"
						v-on:mouseover="hover2=false" style="height: 70px; min-height: 70px;     border-bottom: solid 1px #e6e6e6;"
						v-on:mouseleave="hover2=true" v-on:click="visAddPhrase = false; idVocabulary=vocabularyActive.id">
						<div  style="background: #e6e6e6; position: absolute; width: 100%; height: 100%; transition: 0.5s"
						v-bind:style="{ opacity: !hover2 ? '0.0' : '0.5'}"></div>

						<font-awesome-icon style="margin-right: 15px;" icon="plus" size="2x"/>

						<div v-if="!vocabularyActive.words || vocabularyActive.words.length == 0" class="add-vocab-mobile-text">Добавить первое cлово или словосочетание</div>
					</div>

					<li v-for="item in vocabularyActive.words" :key="item.id" class="list-item">
						<div>
							<div class="list-ul-name">{{item.word}}</div>
						</div>
						<div class="rightpart-list">
							<span v-for="trans in item.translations" :key="trans.id" style="margin-left: 20px;">
								{{trans.translate}}
							</span>
						</div>
					</li>
				</ul>
			</div>
		</div>

		<div class="mat-div" v-if="vocabulary && vocabulary.length>0 && width>=768">
			<div class="mat-title">
				<div class="mat-name">Весь список словарей</div>
				<div>
				</div>
			</div>
			<ul class="list-ul">
				<li v-for="item in vocabulary" :key="item.id" class="list-item">
					<div style="flex: 30%;">
						<div class="list-ul-name">{{item.name}}</div>
						<div class="list-ul-date">{{item.create_time}}</div>
					</div>
					<div style="flex: 30%;">
						<div class="list-ul-name" style="font-weight: 400">{{item.words.length}} из 400 слов</div>
					</div>
					<div class="rightpart-list">

						<div class="button-add" v-on:click="train(item)">Начать тренировку</div>
						<router-link class="button-add" style="margin-left: 10px;" tag="div"
						:to="{path: 'words/' + item.id}">
							<font-awesome-icon icon="bars" />
						</router-link>


						<div class="button-add" style="margin-left: 10px; width: 38px; padding: 0;"
							v-bind:style="{ color: item.like ? '#376bff' : ''}"
							v-on:click="clickLike(item)">
							<font-awesome-icon icon="heart" />
						</div>
					</div>
				</li>
			</ul>
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

		<div class="back-modal" v-if="!visError"></div>
		<div class="mat-modal" v-if="!visError">
			<div class="modal-title">
				Сначала добавьте слова в словарь
			</div>
			<div class="modal-form">
				<div class="modal-form-btns">
					<button class="btn-submit" v-on:click="visError=true">Хорошо</button>
				</div>
			</div>
		</div>

		<div class="back-modal" v-if="!visDeleteVocab"></div>
		<div class="mat-modal" v-if="!visDeleteVocab">
			<div class="modal-title">
				Удалить словарь?
			</div>
			<div class="modal-form">
				<div class="modal-form-btns">
					<button class="btn-cancel" v-on:click="visDeleteVocab = true">Назад</button>
					<button class="btn-submit" v-on:click="deleteVocab()" style="margin-left: 10px;">Удалить</button>
				</div>
			</div>
		</div>

		<NewWord v-bind:idVocabulary="idVocabulary" v-if="!visAddPhrase" @close="visAddPhrase = true" @getData="getData()" />

		<TrainingModal v-bind:vocabulary="vTrainingModal" v-if="vTrainingModal" @close="vTrainingModal = undefined" />
	</div>
</template>

<script>
import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHeart } from '@fortawesome/free-solid-svg-icons'
import { faBook } from '@fortawesome/free-solid-svg-icons'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import { faTrash } from '@fortawesome/free-solid-svg-icons'
import { faBars } from '@fortawesome/free-solid-svg-icons'
import NewWord from '@/components/New-word';
import TrainingModal from '@/components/TrainingModal';
import RPService from '../services/rps';
library.add(faHeart)
library.add(faBook)
library.add(faPlus)
library.add(faTrash)
library.add(faBars)
const rps = new RPService();

export default Vue.extend({
	name: 'Home',
	components: {
		NewWord,
		TrainingModal
	},
	data() {
		return {
			visError: Boolean,
			idVocabulary: Number,
			visAddPhrase: Boolean,
			vTrainingModal: undefined,
			boxes: Boolean,
			hover: Boolean,
			hover2: Boolean,
			visAdd: Boolean,
			visDeleteVocab: Boolean,
			vocabulary: null,
			vocabularyActive: null,
			width: 0,
			vocab: {
				'name': null
			}
		};
	},
	created() {
		this.updateWidth();
		window.addEventListener('resize', this.updateWidth);
		rps.getListVocabulary().then(res => {
			this.vocabulary = res;
			if (this.vocabulary && this.vocabulary.length > 0){
				this.vocabularyActive = this.vocabulary[0];
			}
		});
	},
	methods: {
		addVocabulary() {
			if (this.vocab.name.trim()){
				rps.createVocabulary(this.vocab).then(() => {
					rps.getListVocabulary().then(res => {
						this.vocabulary = res;
						this.visAdd = true;
						this.vocab.name = null;
						if (this.vocabulary && this.vocabulary.length > 0){
							if (!this.vocabularyActive){
								this.vocabularyActive = this.vocabulary[0];
							} else {
								const v = this.vocabulary.filter(x => x.id == this.vocabularyActive.id);
								if (v && v.length > 0){
									this.vocabularyActive = v[0];
								}
							}
						}
					});
				});
			}
		},
		updateWidth() {
			this.width = window.innerWidth;
		},
		clickLike(item){
			item.like = !item.like;
			rps.editVocabulary(item.id, item).then(() => {
				rps.getListVocabulary().then(res => {
					this.vocabulary = res;
					const v = this.vocabulary.filter(x => x.id == this.vocabularyActive.id);
					if (v && v.length > 0){
						this.vocabularyActive = v[0];
					}
				});
			});
		},
		getData(){
			rps.getListVocabulary().then(res => {
				this.vocabulary = res;
					const v = this.vocabulary.filter(x => x.id == this.vocabularyActive.id);
					if (v && v.length > 0){
						this.vocabularyActive = v[0];
					}
			});
		},
		train(item){
			if (item.words?.length > 0){
				this.vTrainingModal=item
			} else {
				this.visError = false;
			}
		},
		deleteVocab(){
			rps.deleteVocabulary(this.vocabularyActive.id).then(res => {
				rps.getListVocabulary().then(res => {
					this.vocabulary = res;
					this.visDeleteVocab = true;
					if (this.vocabulary && this.vocabulary.length > 0){
						this.vocabularyActive = this.vocabulary[0];
					} else {
						this.vocabularyActive = undefined;
					}
				});
			});
		}
	}
});
</script>
