//orders
function TableIncoming() {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/orders/incoming')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
      <td><button onClick={() => ToApprove(item[0])}>Approve</button></td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
          <th>Approve</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
}

function Load_incoming_orders(){
  ReactDOM.render(<TableIncoming />, document.getElementById('container1'));
}

function TableAll() {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/orders/all')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
      <td><button onClick={() => ToApprove(item[0])}>Approve</button></td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
          <th>Approve</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
}

function Load_all_orders(){
  ReactDOM.render(<TableAll />, document.getElementById('container1'));
}

function TableOutcoming() {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/orders/outcoming')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
      <td><button onClick={() => ToApprove(item[0])}>Approve</button></td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
          <th>Approve</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
}

function Load_outcoming_orders(){
  ReactDOM.render(<TableOutcoming />, document.getElementById('container1'));
}

function Make_order(){
  ReactDOM.render(
      <div>
          <form method="post" action="/makeorder" style={{ 
              backgroundColor: 'gray',
              height: '180px',
              margin: '20px',
              width: '300px'
          }}>
              <label htmlFor="client">Client info:</label>
              <input type="text" id="client" name="client" />
              <br /><br />
              <label htmlFor="type">Type:</label>
              <input type="text" id="type" name="type" />
              <br /><br />
              <label htmlFor="date">Date:</label>
              <input type="text" id="date" name="date" />
              <br /><br />
              <label htmlFor="place">Place:</label>
              <input type="text" id="place" name="place" />
              <br /><br />
              <input type="submit" value="Make order" />
          </form>
      </div>,
      document.getElementById('container1')
  );
}

function Load_orders(){
  ReactDOM.render([
    <div>
      <button onClick={Load_all_orders}>All</button>
      <button onClick={Load_incoming_orders}>Incoming</button>
      <button onClick={Load_outcoming_orders}>Outcoming</button>
      <button onClick={Make_order}>Make order</button>
    </div>], document.getElementById('side_bar')
    
  )
}
function ToApprove(id) {
  fetch(`/toapprove/${id}`, {
    method: 'POST',
  });
}

//To approve
function Load_toapprove(){
  ReactDOM.render([
    <div>
      <button onClick={Load_all_orders_to_approve}>All</button>
      <button onClick={Load_incoming_orders_to_approve}>Incoming</button>
      <button onClick={Load_outcoming_orders_to_approve}>Outcoming</button>
    </div>], document.getElementById('side_bar')
  )
}
function TableIncomingToApprove() {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/approvement/incoming')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
      <td><button onClick={() => BackToExisting(item[0])}>Reject</button></td>
      <td><button onClick={() => ToHystory(item[0])}>Approve</button></td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
          <th>Reject</th>
          <th>Approve</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
}

function Load_incoming_orders_to_approve(){
  ReactDOM.render(<TableIncomingToApprove />, document.getElementById('container1'));
}
function TableOutcomingToApprove() {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/approvement/outcoming')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
      <td><button onClick={() => BackToExisting(item[0])}>Reject</button></td>
      <td><button onClick={() => ToHystory(item[0])}>Approve</button></td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
          <th>Reject</th>
          <th>Approve</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
}

function Load_outcoming_orders_to_approve(){
  ReactDOM.render(<TableOutcomingToApprove />, document.getElementById('container1'));
}
function TableAllToApprove() {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/approvement/all')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
      <td><button onClick={() => BackToExisting(item[0])}>Reject</button></td>
      <td><button onClick={() => ToHystory(item[0])}>Approve</button></td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
          <th>Reject</th>
          <th>Approve</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );
}

function Load_all_orders_to_approve(){
  ReactDOM.render(<TableAllToApprove />, document.getElementById('container1'));
}

function BackToExisting(id){
  fetch(`/approve/${id}/reject`, {
    method: 'POST',
  });
}
function ToHystory(id){
  fetch(`/approve/${id}/approve`, {
    method: 'POST',
  });
}
//hystory

function load_hystory(){
  ReactDOM.render([
    <div>
      <button onClick={Load_all_hystory}>All</button>
      <button onClick={Load_incoming_hystory}>Incoming</button>
      <button onClick={Load_outcoming_hystory}>Outcoming</button>
    </div>], document.getElementById('side_bar'))
}
function TableAllHystory(){
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/hystory/all')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );  
}
function Load_all_hystory(){
  ReactDOM.render(<TableAllHystory />, document.getElementById('container1'));
}
function TableIncomingHystory(){
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/hystory/incoming')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );  
}
function Load_incoming_hystory(){
  ReactDOM.render(<TableIncomingHystory />, document.getElementById('container1'));
}
function TableOutcomingHystory(){
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    fetch('/hystory/outcoming')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const rows = data.map((item) => (
    <tr key={item[0]}>
      <td>{item[0]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[3]}</td>
      <td>{item[4]}</td>
    </tr>
  ));

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Client</th>
          <th>Type</th>
          <th>Date</th>
          <th>Place</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  );  
}
function Load_outcoming_hystory(){
  ReactDOM.render(<TableOutcomingHystory />, document.getElementById('container1'));
}