/*
=========================================
Admin Portal Script
=========================================
*/

// Restore Admin Session
window.onload = function () {

    if (sessionStorage.getItem("adminAuth") === "true") {
        showDashboard();
    }

};


// Password Eye Toggle

const eye = document.getElementById("toggleEye");
const passField = document.getElementById("adminPass");

eye.onclick = () => {

    const show = passField.type === "password";

    passField.type = show ? "text" : "password";

    eye.className = show
        ? "fa-regular fa-eye-slash"
        : "fa-regular fa-eye";

};


// Admin Login

async function checkAdmin() {

    const username = document.getElementById("adminUser").value.trim();

    const password = document.getElementById("adminPass").value;

    try {

        const response = await fetch(`${API_BASE}/admin/login`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username,
                password
            })

        });

        const data = await response.json();

        if (data.success) {

            sessionStorage.setItem("adminAuth", "true");

            showDashboard();

        }

        else {

            alert(data.message);

        }

    }

    catch (error) {

        console.error(error);

        alert("Cannot connect to backend.");

    }

}


// Show Dashboard

function showDashboard() {

    document.body.style.display = "block";

    document.getElementById("loginSection").style.display = "none";

    document.getElementById("dashboard").style.display = "block";

    loadUsers();

}


// Load Users

async function loadUsers() {

    const table = document.getElementById("userList");

    table.innerHTML = "";

    try {

        const response = await fetch(`${API_BASE}/admin/users`);

        const data = await response.json();

        if (!data.success) {

            table.innerHTML = `
                <tr>
                    <td colspan="4" style="text-align:center;padding:40px;">
                        ${data.message}
                    </td>
                </tr>
            `;

            return;

        }

        if (data.users.length === 0) {

            table.innerHTML = `
                <tr>
                    <td colspan="4" style="text-align:center;padding:40px;">
                        No Registered Users
                    </td>
                </tr>
            `;

            return;

        }

        data.users.forEach(user => {

            table.innerHTML += `

                <tr>

                    <td><strong>${user.username}</strong></td>

                    <td>${user.email}</td>

                    <td>${user.created_at}</td>

                    <td>

                        <span style="color:green;font-weight:600;">
                            Active
                        </span>

                    </td>

                </tr>

            `;

        });

    }

    catch (error) {

        console.error(error);

        table.innerHTML = `
            <tr>
                <td colspan="4" style="text-align:center;padding:40px;">
                    Unable to connect to backend.
                </td>
            </tr>
        `;

    }

}


// Logout

function adminLogout() {

    sessionStorage.removeItem("adminAuth");

    window.location.href = "index.html";

}