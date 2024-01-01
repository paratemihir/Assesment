import Checklist from "./ASSESMENT/Checklist";
import Cart from "./app/features/Cart";
import { store } from "./app/store";
import { Provider } from "react-redux";

function App() {
  return (
    // <Provider store={store}>
    //   <Cart/>
    // </Provider>
    <Checklist/>
  );
}

export default App;
