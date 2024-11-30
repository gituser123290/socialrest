import { useNavigate } from "react-router-dom";
import axios from "axios";

// const baseURL = "http://localhost:8000";
// const navigate = useNavigate();

function useUserActions() {
    const navigate = useNavigate();
    const baseURL = "http://localhost:8000";
    return {
        login,
        register,
        logout,
        getUser,
        getAccessToken,
        getRefreshToken,
    };

    function login(data) {
        return axios.post(`${baseURL}/auth/login/`,data)
        .then((res) => {
        setUserData(data);
        navigate("/");
        });
    }

    // Function to register the user
    function register(data) {
        try {
            const res = axios.post(`${baseURL}/auth/login/`, data);
            setUserData(res.data);
        } catch (error) {
            console.error("Registration failed:", error);
        
        }
    }

    // Function to logout the user
    function logout(navigate) {
        localStorage.removeItem("auth"); 
        navigate("/login"); 
    }

    // Function to get the user data from local storage
    function getUser() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth.user;
    }

    // Function to get the access token from local storage
    function getAccessToken() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth.access; 
    }

    // Function to get the refresh token from local storage
    function getRefreshToken() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth.refresh;
    }

    // Function to set the user data (tokens and user) in local storage
    function setUserData(res) {
        localStorage.setItem("auth", JSON.stringify({
            access: res.data.access,
            refresh: res.data.refresh,
            user: res.data.user,
        }));
    }
}
export default useUserActions;

