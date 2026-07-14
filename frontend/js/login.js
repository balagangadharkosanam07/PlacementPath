/*
=========================================
Login Page Script
=========================================
*/

// Password Eye Toggle

const toggleBtn = document.getElementById("toggleLoginPass");
const passInput = document.getElementById("loginPass");

toggleBtn.addEventListener("click", () => {

    passInput.type =
        passInput.type === "password"
            ? "text"
            : "password";

    toggleBtn.classList.toggle("fa-eye");
    toggleBtn.classList.toggle("fa-eye-slash");

});


// Login Form

document.getElementById("loginForm").addEventListener("submit", async (e) => {

    e.preventDefault();

    const username = document.getElementById("loginUsername").value.trim();

    const password = document.getElementById("loginPass").value;

    const statusMsg = document.getElementById("statusMsg");

    statusMsg.style.display = "none";

    try {

        const response = await fetch(`${API_BASE}/login`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                username: username,
                password: password

            })

        });

        const data = await response.json();

        if (data.success) {

            localStorage.setItem("token", data.token);

            localStorage.setItem("username", data.user.username);

            localStorage.setItem("loggedIn", "true");

            statusMsg.className = "status-msg success";

            statusMsg.style.display = "block";

            statusMsg.textContent = "Login Successful";

            setTimeout(() => {

                window.location.href = "index.html";

            }, 1000);

        }

        else {

            statusMsg.className = "status-msg error";

            statusMsg.style.display = "block";

            statusMsg.textContent = data.message;

        }

    }

    catch (error) {

        console.error(error);

        statusMsg.className = "status-msg error";

        statusMsg.style.display = "block";

        statusMsg.textContent = "Backend server is not running.";

    }

});