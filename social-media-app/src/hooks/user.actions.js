import axios from "axios";
import { useNavigate } from "react-router-dom";

const useUserActions = () => {
    const navigate = useNavigate();
    const baseURL = "http://localhost:8000";
    // return {
    //     login,
    //     register,
    //     logout,
    //     getUser,
    //     getAccessToken,
    //     getRefreshToken,
    // };

    // Login the user
    async function login(data) {
        try {
            const res = await axios.post(`${baseURL}/auth/login/`, data);
            // Registering the account and tokens in the store
            setUserData(res.data); // Correctly passing res.data
            navigate("/"); // Navigate to home or desired page
        } catch (error) {
            console.error("Login failed:", error);
            // You can handle error, show a notification, or any fallback
        }
    }

    // Logout the user
    function logout() {
        localStorage.removeItem("auth");
        navigate("/login"); // Redirect to login page
    }

    // Get the user
    function getUser() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth ? auth.user : null; // Added check if auth exists
    }

    // Get the access token
    function getAccessToken() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth ? auth.access : null; // Added check if auth exists
    }

    // Get the refresh token
    function getRefreshToken() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth ? auth.refresh : null; // Added check if auth exists
    }

    // Set the access token, refresh token, and user properties in local storage
    function setUserData(data) {
        localStorage.setItem("auth", JSON.stringify({
            access: data.access,
            refresh: data.refresh,
            user: data.user,
        }));
    }
    return {
        login,
        // register,
        logout,
        getUser,
        getAccessToken,
        getRefreshToken,
    };
}

export default useUserActions;
