import axios from 'axios';
import React from 'react';

class App extends React.Component {

  state = {details:[]}

  componentDidMount() {
    let data;
    axios.get('http://localhost:8000').then(res => {
      data = res.data;
      this.setState({details: data});
    })
    .catch(err => {})
  }

  render() {
    return(
      <div>
        <header>Datos generados de Django</header>
        <hr></hr>
        {this.state.details.map((output, id) =>(
          <div key={id}>
            <div>
            <h2>{output.var1}</h2>
            <h3>{output.var2}</h3>
            </div>
          </div>
      ))}
      </div>
    )
  }


}

export default App;
