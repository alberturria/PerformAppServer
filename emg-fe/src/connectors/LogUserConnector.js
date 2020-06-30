import axios from 'axios';
import LogUserConnectorInterface from '../interfaces/connectors/LogUserConnectorIntrerface';

export default class LogUserConnector extends LogUserConnectorInterface {
    constructor(email, password) {
        super();

        this.email = email;
        this.password = password;
        this.userId = null;
        this.url = `http://localhost:8000/log-user`;
    }

    logUser() {
        axios.defaults.withCredentials = true;
        const data = {email: this.email, password: this.password}
        return axios({
          method: 'post',
          url: this.url,
          data: data,
          headers: {
              'Content-Type': 'application/json;charset=utf-8',
          },
          withCredentials: false,
      })
        .then((response) => 
        {
          this.userInfo = {userId: response.data.user_id, username: response.data.username };
        })
        .catch(error => console.log(error))
      
      }

    getUserId(){
      return this.userInfo;
    }

    
}


