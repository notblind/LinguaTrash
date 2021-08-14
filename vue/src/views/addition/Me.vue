<template>
	<div class="me-back">
		<div class="me-back-home">

			<div class="main-info">
				<ul class="main-info-top">
					<li class="name">
						<div>Ли Денис Борисович</div>
						<div>Python Developer / Backend Developer</div>
					</li>


					<li><font-awesome-icon icon="envelope" /><span>denislee98@gmail.com</span></li>
					<li><font-awesome-icon icon="phone" /><span>+7 (918) 235-64-23</span></li>
					<li><font-awesome-icon icon="map-marker" /><span>Санкт-Петербург</span></li>
				</ul>
			</div>

			<div style="display: flex;">
				<div style="width=50%">
					<div class="me-circle">
						<ul class="me-circle-ul">
							<li></li>
							<li></li>
							<li></li>
							<li></li>
							<li></li>
							<li>Backend</li>
						</ul>
						<div class="me-skills">
							Info
						</div>


						<div class="skill skill-1">
							<span class="num">1</span>
							<span class="skill-name">Обо мне</span>
						</div>
						<div class="skill skill-2">
							<span class="num">2</span>
							<span class="skill-name">Образоваине и опыт</span>
						</div>
						<div class="skill skill-3">
							<span class="num">3</span>
							<span class="skill-name">Технические навыки</span>
						</div>
						<div class="skill skill-4">
							<span class="num">4</span>
							<span class="skill-name">Портфолио</span>
						</div>
						<div class="skill skill-5">
							<span class="num">5</span>
							<span class="skill-name">Проекты</span>
						</div>
						<!-- <div class="skill skill-6">
							<span class="num">6</span>
							<span class="skill-name">Frontend</span>
						</div> -->
					</div>
				</div>

				<div class="contant-info">
					<div>
						Образование
						Санкт-Петербургский государственный электротехнический университет имени В.И. Ленина
						Информационные системы и технологии
						Квалификация	Бакалавр

						Опыт работы
						февраль 2020 (подсчет месяцев)
					</div>
				</div>
			</div>

			<div style="color: white;" class="bottom-line">
				<div>Для более тесного общения</div>
				<div><font-awesome-icon :icon="{ prefix: 'fab', iconName: 'vk' }"/></div>
				<div><font-awesome-icon :icon="{ prefix: 'fab', iconName: 'instagram' }"/></div>
				<div><font-awesome-icon :icon="{ prefix: 'fab', iconName: 'telegram' }"/></div>
			</div>



		</div>
	</div>
</template>

<script>

import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'
import { faPhone } from '@fortawesome/free-solid-svg-icons'
import { faMapMarker } from '@fortawesome/free-solid-svg-icons'
import { faVk } from '@fortawesome/free-brands-svg-icons'
import { faInstagram } from '@fortawesome/free-brands-svg-icons'
import { faTelegram } from '@fortawesome/free-brands-svg-icons'

library.add(faTelegram)
library.add(faVk)
library.add(faInstagram)
library.add(faEnvelope)
library.add(faPhone)
library.add(faMapMarker)

export default Vue.extend({
	name: 'Me',
	components: {
	},
	methods: {
		con(){
			console.info('dsadasda');
		}
	}
});
</script>