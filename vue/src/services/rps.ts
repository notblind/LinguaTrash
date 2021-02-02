import axios from 'axios';

export default class RPService {

	_data: any;
	res: any;
	_jwtToken: any;

	_getJWTToken(){
		if (!this._jwtToken){
			const results = document.cookie.match ( '(^|;) ?' + 'jwt' + '=([^;]*)(;|$)' );
			return results ? results[2] : '';
		} else return this._jwtToken;
	}

	_delJWTToken(){
		const cookieDate = new Date ();
		cookieDate.setTime(cookieDate.getTime() - 1);
		document.cookie = "jwt=; expires=" + cookieDate.toUTCString();
	}

	sendRequest(url: string, method: string, data: any): Promise<any>{
		const config = {
			headers: {
				'Authorization': 'Bearer ' + this._getJWTToken(),
			}
		}
		console.info(this._getJWTToken());
		return axios.post('http://localhost:8000/' + url, {method: method, data: data}, config).catch(function (error) {
		if (error.response) {
			// Request made and server responded
			console.log(error.response.data);
			console.log(error.response.status);
			console.log(error.response.headers);
			if (error.response.status == '401'){
				// TODO: сделать проверку на url  и только тогда редиректить
				window.location.replace("http://localhost:8080/login");
			}
		} else if (error.request) {
			// The request was made but no response was received
			console.log(error.request);
		} else {
			// Something happened in setting up the request that triggered an Error
			console.log('Error', error.message);
		}

	});
	}

	_login(username: any, password: any): Promise<any>{
		const bodyFormData = new FormData();
		bodyFormData.append('username', username);
		bodyFormData.append('password', password);
		return axios.post('http://localhost:8000/auth/jwt/create', bodyFormData)
	}

	logIn(username: any, password: any){
		this._data = this._login(username, password).then(res =>{
			this._jwtToken = res.data.access;
			document.cookie = "jwt="+ this._jwtToken +"; max-age=3600;";
			console.info( document.cookie );
		});
		return this._data
	}

	_sigup(username: any, password: any): Promise<any>{
		const bodyFormData = new FormData();
		bodyFormData.append('username', username);
		bodyFormData.append('password', password);
		bodyFormData.append('email', username);
		return axios.post('http://localhost:8000/auth/users/', bodyFormData)
	}

	signUp(username: any, password: any){
		this._data = this._sigup(username, password);
		return this._data
	}

	logOut(): Promise<any>{
		this._jwtToken = undefined;
		this._delJWTToken();
		console.info(this._getJWTToken());
		return this._data
	}

	getMeOnly(): Promise<any>{
		const config = {
			headers: {
				'Authorization': 'Bearer ' + this._getJWTToken(),
			}
		}
		return axios.post('http://localhost:8000/api/vocabulary/partner', {method: 'get_me', data: {}}, config)
	}

	getMe(): Promise<any>{
		this._data = this.sendRequest('api/vocabulary/partner', 'get_me', {});
		return this._data
	}

	getVocabulary(): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'get_vocabulary', {});
		return this._data
	}

	getOneVocabulary(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'get_one_vocabulary', {idVocabulary: idVocabulary});
		return this._data
	}

	getWords(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'get_words', {idVocabulary: idVocabulary});
		return this._data
	}

	createVocabulary(vocabulary: any): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'create_vocabulary', {vocabulary: vocabulary});
		return this._data
	}

	editVocabulary(vocabulary: any): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'edit_vocabulary', {vocabulary: vocabulary});
		return this._data
	}

	createWord(word: any): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'create_word', {word: word});
		return this._data
	}

}