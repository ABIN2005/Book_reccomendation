const recommendationsData = {
    "suspense": [
        { title: "Gone Girl by Gillian Flynn", description: "A thriller that follows a man who becomes the prime suspect in the disappearance of his wife." },
        { title: "The Girl on the Train by Paula Hawkins", description: "A psychological thriller about a woman who becomes entangled in a missing persons investigation." }
    ],
    "thrillers": [
        { title: "The Da Vinci Code by Dan Brown", description: "A mystery thriller that follows a symbologist's quest for the Holy Grail." },
        { title: "The Silent Patient by Alex Michaelides", description: "A psychological thriller about a woman's act of violence against her husband." }
    ],
    "romance": [
        { title: "Pride and Prejudice by Jane Austen", description: "A classic romance that explores themes of love and social class." },
        { title: "The Notebook by Nicholas Sparks", description: "A love story that follows a couple through decades of ups and downs." }
    ],
    "science fiction": [
        { title: "Dune by Frank Herbert", description: "A science fiction novel set in a desert planet, where the protagonist becomes embroiled in a power struggle." },
        { title: "The Martian by Andy Weir", description: "A story about an astronaut stranded on Mars and his struggle to survive." },
        { title: "The Hitchhiker's Guide to the Galaxy by Douglas Adams", description: "A humorous science fiction series about the adventures of an unwitting human." }
    ],
    // Add more genres and books as needed
};

document.getElementById("recommend-btn").addEventListener("click", function() {
    const genreInput = document.getElementById("genre-input").value.toLowerCase();
    const recommendationList = document.getElementById("recommendation-list");
    const recommendationsDiv = document.getElementById("recommendations");
    
    recommendationList.innerHTML = ""; // Clear previous recommendations

    if (recommendationsData[genreInput]) {
        recommendationsData[genreInput].forEach(book => {
            const listItem = document.createElement("li");
            listItem.innerHTML = `<h3>${book.title}</h3><p>${book.description}</p>`;
            recommendationList.appendChild(listItem);
        });

        recommendationsDiv.style.display = "block"; // Show recommendations div
        setTimeout(() => { recommendationsDiv.style.opacity = 1; }, 10); // Fade in effect
    } else {
        recommendationList.innerHTML = "<li>No recommendations found for this genre.</li>";
        recommendationsDiv.style.display = "block";
        recommendationsDiv.style.opacity = 1; // Ensure visibility
    }
});
