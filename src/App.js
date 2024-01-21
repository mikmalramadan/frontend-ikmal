import { BrowserRouter, Routes, Route} from "react-router-dom";
import UserList from "./componen/UserList";
import AddUser from "./componen/AddUser"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UserList/>}/>
        <Route path="add" element={<AddUser/>}/>   
      </Routes>
    </BrowserRouter>
  );
}

export default App;
