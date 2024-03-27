function Login() {
  function logout() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refresh_token');
    window.location.href = '/login';
  }
  return (
    <div>
      {logout()}
    </div>
  );
}

export default Login;
