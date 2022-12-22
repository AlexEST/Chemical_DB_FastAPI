


const authProvider = {
    login: ({ username, password }) =>  {
        const request = new Request('http://localhost:8000/token', {
            method: 'POST',
            body: JSON.stringify({ username, password }),
            headers: new Headers({ 'Content-Type': 'application/json' }),
        });       
        return fetch(request)
            .then(response => {
                if (response.status < 200 || response.status >= 300) {
                    throw new Error(response.statusText);
                }
                return response.json();
            })
            .then(auth => {
                localStorage.setItem('username', username)
                localStorage.setItem('auth', JSON.stringify(auth));
                return Promise.resolve();
            })
            .catch(() => {
                throw new Error('Wrong password or login')
            });
            
    },
    checkError: (error) => {
        const status = error.status;
        if (status === 401 || status === 403) {
            localStorage.removeItem('auth');
            return Promise.reject();
        }
        // other error code (404, 500, etc): no need to log out
        return Promise.resolve();
    },
    checkAuth: () =>
        localStorage.getItem('username') ? Promise.resolve() : Promise.reject(),
    getPermissions: () => {
        // Required for the authentication to work
        return Promise.resolve();
    },
    logout: () => {
        localStorage.removeItem('username');
        return Promise.resolve();
    },
    getIdentity: () => {
        try {
            const {id, fullName, avatar } = JSON.parse(localStorage.getItem('auth'));
            return Promise.resolve({ fullName });
        } catch (error) {
            return Promise.reject(error);
        }
    },
    getPermissions: () => {
        const role = localStorage.getItem('permissions');
        return role ? Promise.resolve(role) : Promise.reject();
    }
};

export default authProvider;