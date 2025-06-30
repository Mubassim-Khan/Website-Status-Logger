document.getElementById("refresh-btn").addEventListener("click", function () {
  // Fetching data message
  document.getElementById("fetching-status-message").style.display = "flex";

  fetch("/refresh")
    .then((response) => response.json())
    .then((data) => {
      // Update last refreshed
      document.getElementById("last-refreshed").textContent =
        data.last_refreshed;
      console.log("Button Clicked");

      // Update social media table
      let socialTable = document.getElementById("social-media-table");
      let socialRows = "";
      for (const [url, info] of Object.entries(data.statuses.social_media)) {
        socialRows += `<tr class="data-row">
          <td class="site-name">${info.name}</td>
          <td><a href="${url}" target="_blank">${url}</a></td>
          <td class="${
            info.status === "OK"
              ? "status--ok"
              : info.status.includes("Error")
              ? "status--error"
              : "status--down"
          } status">
            ${info.status}
          </td>
          <td class="status">${info.last_checked}</td>
        </tr>`;
      }
      // Replace all rows except the header
      socialTable.innerHTML =
        `<tr>
        <th class="table-heading" scope="col">Site Name</th>
        <th class="table-heading" scope="col">URL</th>
        <th class="table-heading" scope="col">Status</th>
        <th class="table-heading" scope="col">Last Checked</th>
      </tr>` + socialRows;

      // Update projects table
      let projectsTable = document.getElementById("projects-table");
      let projectRows = "";
      for (const [url, info] of Object.entries(data.statuses.projects)) {
        projectRows += `<tr class="data-row">
          <td class="site-name">${info.name}</td>
          <td><a href="${url}" target="_blank">${url}</a></td>
          <td class="${
            info.status === "OK"
              ? "status--ok"
              : info.status.includes("Error")
              ? "status--error"
              : "status--down"
          } status">
            ${info.status}
          </td>
          <td class="status">${info.last_checked}</td>
        </tr>`;
      }
      projectsTable.innerHTML =
        `<tr>
        <th class="table-heading" scope="col">Site Name</th>
        <th class="table-heading" scope="col">URL</th>
        <th class="table-heading" scope="col">Status</th>
        <th class="table-heading" scope="col">Last Checked</th>
      </tr>` + projectRows;
    })
    .finally(() => {
      // Hide the fetching data msg
      document.getElementById("fetching-status-message").style.display = "none";
    });
});
