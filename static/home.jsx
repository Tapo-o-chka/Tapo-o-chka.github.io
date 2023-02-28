function load_home(){
    ReactDOM.render([
      <h1>Hello, home</h1>,
      <h2>Subheading 1</h2>,
      <h3>Subheading 2</h3>],
        document.getElementById('container1'))
}
function load_about(){
    ReactDOM.render([
        <h1 style={{float:"right"}}>Hello, about</h1>],
        document.getElementById('container1'))
}
function load_login(){
    ReactDOM.render(
        <div>
            <form method="post" action="/login" style={{ 
                backgroundColor: 'gray',
                height: '180px',
                margin: '20px',
                width: '300px'
            }}>
                <label htmlFor="login">Username:</label>
                <input type="text" id="login" name="login" />
                <br /><br />
                <label htmlFor="password">Password:</label>
                <input type="password" id="password" name="password" />
                <br /><br />
                <input type="submit" value="Login" />
            </form>
            <form method="post" action="/register" style={{ 
                backgroundColor: 'gray',
                height: '180px',
                margin: '20px',
                width: '300px'
            }}>
                <label htmlFor="login">Username:</label>
                <input type="text" id="login" name="login" />
                <br /><br />
                <label htmlFor="password">Password:</label>
                <input type="password" id="password" name="password" />
                <br /><br />
                <label htmlFor="email">Email:</label>
                <input type="text" id="email" name="email" />
                <br /><br />
                <input type="submit" value="Register" />
            </form>
        </div>,
        document.getElementById('container1')
    );
}
