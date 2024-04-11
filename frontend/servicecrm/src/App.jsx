import './App.css';
import NavigationBar from './components/NavigationBar';
import Table from './components/Table';
import MyButton from './components/Btn';
import 'bootstrap/dist/css/bootstrap.css';



function App() {
  return (
    <div className="App">
       <NavigationBar/>
         <Table/>
       <MyButton/>
    </div>
  );
}

export default App;
