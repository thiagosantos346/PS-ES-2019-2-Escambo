import React from 'react';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

function Login() {

    return (
        <form noValidate autoComplete="off">
        <TextField 
            id="username"
            label="Usuário"
            variant="outlined"
            autoFocus="true"
            multiline="false"
            margin="dense"
            fullWidth="true"
            />
        <TextField 
            id="Senha"
            label="Senha"
            variant="outlined"
            type="password"
            multiline="false"
            margin="dense"
            fullWidth="true"
            />
            <Button
                id='send'
                variant="contained"
                color="primary"
                fullWidth="true"
                >
            Entrar
            </Button>
            <Button
                id='createAccount'
                variant="outlined"
                color="secondary"
                fullWidth='true'
                >
            Inscrever-se
            </Button>
            <Button
                id='losePassword'
                variant="text"
                color="inherit"
                fullWidth='true'
                >
            esqueceu a senha?
            </Button>
        </form>
    )
}

export default Login;