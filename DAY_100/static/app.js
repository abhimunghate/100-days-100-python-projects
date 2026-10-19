const list = document.querySelector("#tasks");
const form = document.querySelector("#task-form");

async function load() {
  const response = await fetch("/api/tasks");
  const data = await response.json();

  list.innerHTML = "";
  data.tasks.forEach((task) => {
    const item = document.createElement("li");
    item.className = task.completed ? "done" : "";
    item.textContent = task.title;
    item.onclick = async () => {
      await fetch(`/api/tasks/${task.id}`, { method: "PATCH" });
      load();
    };
    list.appendChild(item);
  });
}

form.onsubmit = async (event) => {
  event.preventDefault();

  const title = document.querySelector("#title");
  await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: title.value }),
  });

  title.value = "";
  load();
};

load();

// Done