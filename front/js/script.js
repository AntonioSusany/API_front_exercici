document.addEventListener("DOMContentLoaded", function() {
    console.log("Intentando cargar los alumnos...");
    fetch("http://localhost:8000/alumnes/list")
        .then(response => {
            if (!response.ok) {
                throw new Error("Error a la resposta del servidor");
            }
            return response.json();
        })
        .then(data => {
            console.log("Datos recibidos:", data); 
            const alumnesTableBody = document.querySelector("#tablaAlumne tbody");
            alumnesTableBody.innerHTML = "";

            
            data.forEach(alumne => {
                const row = document.createElement("tr");

                const idCell = document.createElement("td");
                idCell.textContent = alumne.IdAlumne;
                row.appendChild(idCell);

                const idAulaCell = document.createElement("td");
                idAulaCell.textContent = alumne.IdAula;
                row.appendChild(idAulaCell);

                const nomCell = document.createElement("td");
                nomCell.textContent = alumne.NomAlumne; 
                row.appendChild(nomCell);

                const cicleCell = document.createElement("td");
                cicleCell.textContent = alumne.Cicle;
                row.appendChild(cicleCell);

                const cursCell = document.createElement("td");
                cursCell.textContent = alumne.Curs;
                row.appendChild(cursCell);

                const grupCell = document.createElement("td");
                grupCell.textContent = alumne.Grup; 
                row.appendChild(grupCell);

                alumnesTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error("Error capturat:", error);
            alert("Error al carregar la llista d'alumnes");
        });
});

