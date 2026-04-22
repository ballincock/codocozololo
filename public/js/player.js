  const playlist = < %= @playlist_json % > ;
  let index = Math.floor(Math.random() * playlist.length); 

  const audio = document.getElementById('audio-ctrl');
  const bg = document.getElementById('main-bg');
  const title = document.getElementById('display-title');

  function playNext() {
      const song = playlist[index];
      title.innerText = song.title;
      audio.src = song.audio;
      bg.style.backgroundImage = `url('${song.image}')`; 
      audio.play();
      index = (index + 1) % playlist.length; 
  }

  audio.onended = playNext;

  playNext();

  function askConch() {
      const answers = ["Maybe someday.", "Nothing.", "Follow the money.", "I don't think so.", "Try asking again."];
      const random = answers[Math.floor(Math.random() * answers.length)];
      document.getElementById('conchMessage').innerText = random;
      document.getElementById('conchModal').style.display = 'flex';
  }

  function closeConch() {
      document.getElementById('conchModal').style.display = 'none';
  }
