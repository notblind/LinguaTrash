<template>
	<div class="home" style="margin-bottom:60px; margin-top: 10px;">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">Тренировка</div>
				<div class="button-add" v-on:click="visClose = false">Завершить
				</div>
			</div>
		</div>

		<div class="loader" v-if="!currentItem"></div>

		<div class="training-box" v-if="currentItem">
			<div class="training-box-item" v-on:mouseover="hover2=true" v-on:mouseleave="hover2=false"
				v-on:click="currentIndex!=0 ? prevWord() : ''"
				v-bind:style="{ 'cursor': currentIndex!=0 ?  'pointer' : ''}">
				<div class="training-back button-add" v-if="currentIndex!=0"
					v-bind:class="{ 'button-add-hov': hover2}">Предыдущее слово</div>
				<div class="training-solve">
					{{currentItem.word}}
				</div>
			</div>

			<div class="training-box-item" v-on:mouseover="hover1=true" v-on:mouseleave="hover1=false"
				v-on:click="currentMode=='first' ? nextWord() : ''"
				style="cursor: pointer;">

				<div class="training-next button-add" 
					v-if="currentIndex+1!=training.length && (currentMode=='first' || ch)" v-bind:class="{ 'button-add-hov': hover1}">Следующее слово</div>

				<div class="training-next button-add" 
					v-if="currentIndex+1==training.length && (currentMode=='first' || ch)" v-bind:class="{ 'button-add-hov': hover1}">Дальше</div>
				<div class="training-solve" v-if="currentMode=='first'" style="text-align: center;">
					<div v-for="trans in currentItem.translations" :key="trans.id">
						{{trans.translate}}
					</div>
				</div>
				<div class="training-solve-ch" v-if="currentMode=='second' || currentMode=='third'">
					<div v-for="(item, index) in currentItem.options" :key="item.option"
						v-on:click="!ch ? ch = item : nextWord()"
						v-bind:style="{ 'height': 'calc(100% / ' + String(currentItem.options.length) + ')',
						'background': ch && item.right ? '#98FB98' : ch==item && !item.right ? '#FFA07A' : '',
						'width': ch ? 'calc(100% - 49px)' : ''}">
						{{index+1}}. {{item.option}}
					</div>
				</div>
			</div>
		</div>

		<div class="training-progress" v-if="currentItem && width>=768">
			<div v-if="!this.modes || this.modes.first" class="progress-bar progress-f">
				<div class="load-f"
					v-bind:style="{ 'width': 'calc(100% * ' + String(loadF) + ' / ' +String(length) + ')'}"></div>
				Карточки со словами
			</div>
			<div v-if="!this.modes || this.modes.second" class="progress-bar progress-s">
				<div class="load-s"
					v-bind:style="{ 'width': 'calc(100% * ' + String(loadS) + ' / ' +String(length) + ')'}"></div>
				Перевод слов
			</div>
			<div v-if="!this.modes || this.modes.third" class="progress-bar progress-t">
				<div class="load-t"
					v-bind:style="{ 'width': 'calc(100% * ' + String(loadT) + ' / ' +String(length) + ')'}"></div>
				Обратный перевод слов
			</div>
		</div>

		<div class="training-progress" v-if="currentItem && width<768">
			<div v-if="this.currentMode=='first' && (!this.modes || this.modes.first)" class="progress-bar progress-f">
				<div class="load-f"
					v-bind:style="{ 'width': 'calc(100% * ' + String(loadF) + ' / ' +String(length-1) + ')'}"></div>
				Карточки со словами
			</div>
			<div v-if="this.currentMode=='second' && (!this.modes || this.modes.second)" class="progress-bar progress-s">
				<div class="load-s"
					v-bind:style="{ 'width': 'calc(100% * ' + String(loadS) + ' / ' +String(length-1) + ')'}"></div>
				Перевод слов
			</div>
			<div v-if="this.currentMode=='third' && (!this.modes || this.modes.third)" class="progress-bar progress-t">
				<div class="load-t"
					v-bind:style="{ 'width': 'calc(100% * ' + String(loadT) + ' / ' +String(length-1) + ')'}"></div>
				Обратный перевод слов
			</div>
		</div>

		<div class="back-modal" v-if="!visClose"></div>
		<div class="mat-modal" v-if="!visClose">
			<div class="modal-title">
				Тренировка завершена
			</div>
			<div class="modal-form">
				<div class="modal-form-btns">
					<button class="btn-cancel" v-on:click="endTraining()">Завершить</button>
					<button class="btn-submit" v-on:click="init()" style="margin-left: 10px;">Повторить</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../services/rps';
const rps = new RPService();
import router from  '../router/index.ts'

export default Vue.extend({
	name: 'Training',
	components: {
	},
	props: ['modes'],
	computed: {
    idVocabulary() {
      return this.$route.params.idVocabulary;
    },
  },
  data() {
		return {
			loadF: 0,
			loadS: 0,
			loadT: 0,
			width: 0,
			length: Number,
			visClose: Boolean,
			hover1: Boolean,
			hover2: Boolean,
			currentMode: null,
			currentItem: null,
			ch: null,
			currentIndex: Number,
			training: []
		};
	},
	created() {
		this.updateWidth();
		window.addEventListener('resize', this.updateWidth);
		this.hover1 = false;
		this.hover2 = false;
		rps.getOneVocabulary(this.idVocabulary).then(res => {
			if (res.data.vocabulary){
				this.length = res.data.vocabulary.ammount;
			}
		});
		this.changeMode();
	},
	methods: {
		updateWidth() {
			this.width = window.innerWidth;
		},
		init(){
			this.visClose = true;
			this.hover1 = false;
			this.hover2 = false;
			this.currentMode = null;
			this.currentItem = null;
			this.ch = null;
			this.currentIndex = undefined;
			this.training = [];
			this.changeMode();
		},
		changeMode(){
			this.ch = false;
			if (this.currentMode=='first'){
				if (!this.modes || this.modes.second){
					this.currentMode='second'
				} else if (this.modes.third){
					this.currentMode='third'
				} else {
					this.visClose = false;
				}
			} else if (this.currentMode=='second'){
				if (!this.modes || this.modes.third){
					this.currentMode='third'
				} else {
					this.visClose = false;
				}
			} else if (this.currentMode=='third'){
				this.visClose = false;
			} else {
				if (!this.modes || this.modes.first){
					this.currentMode='first'
				} else 
				if (this.modes.second){
					this.currentMode='second'
				} else if (this.modes.third){
					this.currentMode='third'
				} else {
					this.visClose = false;
				}
			}
			this.startMode();
		},
		startMode(){
			if (this.currentMode=='first'){
				this.modeFirst();
			} else if (this.currentMode=='second'){
				this.modeSecond();
			} else if (this.currentMode=='third'){
				this.modeTrird();
			}
		},
		modeFirst(){
			rps.modeFirst(this.idVocabulary).then(res => {
				this.training = res.data.training;
				if (this.training && this.training.length > 0){
					this.currentItem = this.training[0];
					this.currentIndex = 0;
				}
			});
		},
		modeSecond(){
			rps.modeSecond(this.idVocabulary).then(res => {
				this.training = res.data.training;
				if (this.training && this.training.length > 0){
					this.currentItem = this.training[0];
					this.currentIndex = 0;
				}
			});
		},
		modeTrird(){
			rps.modeTrird(this.idVocabulary).then(res => {
				this.training = res.data.training;
				if (this.training && this.training.length > 0){
					this.currentItem = this.training[0];
					this.currentIndex = 0;
				}
			});
		},
		endTraining(){
			router.push({ name: 'Home' })
		},
		nextWord(){
			if (this.currentMode=='first'){
				this.loadF += 1;
			} else if (this.currentMode=='second'){
				this.loadS += 1;
			} else if (this.currentMode=='third'){
				this.loadT += 1;
			}
			this.currentIndex += 1;
			if (this.currentIndex == this.training.length){
				this.changeMode();
			} else {
				this.currentItem = this.training[this.currentIndex];
			}
			this.ch = false;
		},
		prevWord(){
			if (this.currentMode=='first'){
				this.loadF -= 1;
			} else if (this.currentMode=='second'){
				this.loadS -= 1;
			} else if (this.currentMode=='third'){
				this.loadT -= 1;
			}
			this.ch = false;
			this.currentIndex -= 1;
			this.currentItem = this.training[this.currentIndex];
		}
	}
});
</script>