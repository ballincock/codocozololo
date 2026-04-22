 var map, allPins = [],
        markersLayer, tempMarker;

    window.onload = function() {
        map = L.map('map').setView([39.8, -98.5], 4);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
        markersLayer = L.layerGroup().addTo(map);

        map.on('click', function(e) {
            if (tempMarker) map.removeLayer(tempMarker);
            tempMarker = L.circleMarker(e.latlng, {
                radius: 10,
                color: '#27ae60'
            }).addTo(map);
            document.getElementById('add-form').style.display = 'block';
        });

        loadData();
        setTimeout(() => {
            map.invalidateSize();
        }, 400);
    };

    async function loadData() {
        try {
            credentials: 'include'
            const res = await fetch('/api/pins');
            allPins = await res.json();
            renderUI(allPins);
        }
        catch (e) {
            console.error("Fetch error.");
        }
    }

    function renderUI(data) {
        markersLayer.clearLayers();
        const listDiv = document.getElementById('list-render');
        listDiv.innerHTML = '';
        data.forEach(pin => {
            const m = L.circleMarker([pin.lat, pin.lng], {
                radius: 8,
                fillColor: "#27ae60",
                color: "#000",
                weight: 1,
                fillOpacity: 0.8
            }).addTo(markersLayer).bindPopup(`<b>${pin.location_name}</b>`);
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `<span class="del-btn" onclick="event.stopPropagation(); deletePin(${pin.id})">✖</span><strong>${pin.location_name}</strong><br><small>${pin.species}</small>`;
            card.onclick = () => {
                map.setView([pin.lat, pin.lng], 14);
                m.openPopup();
            };
            listDiv.appendChild(card);
        });
    }

    async function saveNewPin() {
        if (!tempMarker) return;
        const payload = {
            lat: tempMarker.getLatLng().lat,
            lng: tempMarker.getLatLng().lng,
            location_name: document.getElementById('loc_name').value || "New Spot",
            species: document.getElementById('species').value || "None",
            season: document.getElementById('season').value || "N/A",
            time_of_day: document.getElementById('time').value || "N/A",
            lure_used: document.getElementById('lure').value || "N/A"
        };
        await fetch('/api/pins', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        location.reload();
    }

    async function deletePin(id) {
        if (confirm("Delete Pin?")) {
            await fetch(`/api/deletepin/${id}`, {
                method: 'DELETE'
            });
            loadData();
        }
    }

    function filterPins() {
        const term = document.getElementById('search').value.toLowerCase();
        renderUI(allPins.filter(p => (p.species || "").toLowerCase().includes(term) || (p.location_name || "").toLowerCase().includes(term)));
    }

    function closeForm() {
        document.getElementById('add-form').style.display = 'none';
        if (tempMarker) map.removeLayer(tempMarker);
    }
