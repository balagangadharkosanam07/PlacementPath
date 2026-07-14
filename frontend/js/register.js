/*
=========================================
Register Page Script
=========================================
*/

// Password Eye Toggle

const toggleBtn = document.getElementById("toggleRegPass");
const passInput = document.getElementById("password");

toggleBtn.addEventListener("click", () => {

    passInput.type =
        passInput.type === "password"
            ? "text"
            : "password";

    toggleBtn.classList.toggle("fa-eye");
    toggleBtn.classList.toggle("fa-eye-slash");

});


// Register Form

document.getElementById("regForm").addEventListener("submit", async (e) => {

    e.preventDefault();

    const username = document.getElementById("username").value.trim();

    const email = document.getElementById("email").value.trim();

    const password = document.getElementById("password").value;

    const statusMsg = document.getElementById("statusMsg");

    statusMsg.style.display = "none";

    try {

        const response = await fetch(`${API_BASE}/register`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                username: username,
                email: email,
                password: password

            })

        });

        const data = await response.json();

        if (data.success) {

            statusMsg.className = "status-msg success";

            statusMsg.style.display = "block";

            statusMsg.textContent = data.message;

            document.getElementById("regForm").reset();

            setTimeout(() => {

                window.location.href = "login.html";

            }, 1500);

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