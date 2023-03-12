import logo from './logo.svg';
import './App.css';
import Header from './content/header/Header';
import Footer from './content/footer/Footer';

const testStyle = {
  "height": "600px"
}

function App() {
  return (
    <div className="App">
      <Header />
      <div style={testStyle}></div>
      <Footer />
    </div>
  );
}

export default App;
