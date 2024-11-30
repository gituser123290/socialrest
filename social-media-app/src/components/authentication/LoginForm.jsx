// import React, { useState } from "react";
// import { Form, Button } from "react-bootstrap";
// import {useUserActions} from "../../hooks/user.actions";
// import axios from "axios";
// import { useNavigate } from "react-router-dom";

// function LoginForm() {
//     const navigate = useNavigate();
//     const [validated, setValidated] = useState(false);
//     const [form, setForm] = useState({});
//     const [error, setError] = useState(null);
//     const userActions = useUserActions();

//     const handleSubmit = (event) => {
//         event.preventDefault();
//         const loginForm = event.currentTarget;

//         if (loginForm.checkValidity() === false) {
//             event.stopPropagation();
//         }
//         setValidated(true);
//         const data = {
//             email: form.email,
//             password: form.password,
//         };
//         userActions.login(data)
//         axios.post("http://localhost:8000/auth/login/", data)
//             .then((res) => {
//                 // Registering the account and tokens in the store
//                 localStorage.setItem("auth", JSON.stringify({
//                     access: res.data.access,
//                     refresh: res.data.refresh,
//                     user: res.data.user,
//                 }));
//                 navigate("/");
//             })
//             .catch((err) => {
//                 if (err.message) {
//                     setError(err.request.response);
//                 }
//             });
//     };

//     return (
//         <Form
//             id="registration-form"
//             className="border p-4 rounded"
//             noValidate
//             validated={validated}
//             onSubmit={handleSubmit}
//         >
//             <Form.Group className="mb-3">
//                 <Form.Label>Email</Form.Label>
//                 <Form.Control
//                     value={form.email}
//                     onChange={(e) => setForm({ ...form, email: e.target.value })}
//                     required
//                     type="email"
//                     placeholder="Enter Your Email"
//                 />
//                 <Form.Control.Feedback type="invalid">
//                     This field is required.
//                 </Form.Control.Feedback>
//             </Form.Group>

//             <Form.Group className="mb-3">
//                 <Form.Label>Password</Form.Label>
//                 <Form.Control
//                     value={form.password}
//                     minLength="8"
//                     onChange={(e) => setForm({ ...form, password: e.target.value })}
//                     required
//                     type="password"
//                     placeholder="Password"
//                 />
//                 <Form.Control.Feedback type="invalid">
//                     Please provide a valid password.
//                 </Form.Control.Feedback>
//             </Form.Group>

//             <div className="text-content text-danger">
//                 {error && <p>{error}</p>}
//             </div>

//             <Button variant="primary" type="submit">
//                 Submit
//             </Button>
//         </Form>
//     );
// }

// export default LoginForm;

import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import  useUserActions  from "../../hooks/user.actions";
import { useNavigate } from "react-router-dom";
import axiosService from "../../helpers/axios";

function LoginForm() {
    const navigate = useNavigate();
    const [validated, setValidated] = useState(false);
    const [form, setForm] = useState({});
    const [error, setError] = useState(null);
    const userActions = useUserActions();  // This hook is correctly placed here.

    const handleSubmit = (event) => {
        event.preventDefault();
        const loginForm = event.currentTarget;

        if (loginForm.checkValidity() === false) {
            event.stopPropagation();
        }
        setValidated(true);
        
        const data = {
            email: form.email,
            password: form.password,
        };

        // If userActions.login is responsible for handling the request
        userActions.login(data)
        axiosService.post("/auth/login/", data)
            .then((res) => {
                // If login is successful, store tokens in localStorage
                localStorage.setItem("auth", JSON.stringify({
                    access: res.data.access,
                    refresh: res.data.refresh,
                    user: res.data.user,
                }));
                console.log("This is login data",res.data.user,"Access token", res.data.access,"refresh token", res.data.refresh);
                
                navigate("/");
            })
            .catch((err) => {
                // Handle errors during login
                if (err.response) {
                    setError(err.response.data.message || "An error occurred");
                } else {
                    setError("Network error or server unavailable");
                }
            });
    };

    return (
        <Form
            id="registration-form"
            className="border p-4 rounded"
            noValidate
            validated={validated}
            onSubmit={handleSubmit}
        >
            <Form.Group className="mb-3">
                <Form.Label>Email</Form.Label>
                <Form.Control
                    value={form.email}
                    onChange={(e) => setForm({ ...form, email: e.target.value })}
                    required
                    type="email"
                    placeholder="Enter Your Email"
                />
                <Form.Control.Feedback type="invalid">
                    This field is required.
                </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label>Password</Form.Label>
                <Form.Control
                    value={form.password}
                    minLength="8"
                    onChange={(e) => setForm({ ...form, password: e.target.value })}
                    required
                    type="password"
                    placeholder="Password"
                />
                <Form.Control.Feedback type="invalid">
                    Please provide a valid password.
                </Form.Control.Feedback>
            </Form.Group>

            <div className="text-content text-danger">
                {error && <p>{error}</p>}
            </div>

            <Button variant="primary" type="submit">
                Submit
            </Button>
        </Form>
    );
}

export default LoginForm;

