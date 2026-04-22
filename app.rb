require 'sinatra'
require 'digest'
require 'json'

set :port, 4567

def valid_user?(name, auth_token)
  return false if name.nil? || auth_token.nil?
  expected = Digest::MD5.hexdigest("#{name}SECRET_SALT")
  auth_token == expected
end

helpers do
  def get_vibe
    hour = Time.now.hour
    return "Midnight Mystery" if hour < 6
    return "Morning Glow" if hour < 12
    "Ethereal Evening"
  end
end

not_found do
  @error_msg = "Eughh... Who put you on the planet?"
  erb :error
end

error do
  @error_msg = "You failed to respect the conch."
  erb :error
end

before do
  @timestamp = Time.now.strftime("%H:%M:%S")
  puts "[#{@timestamp}] INFO: #{@name || 'Guest'} ascended"
end

get '/ectoplasm/' do
  @vibe = get_vibe
  @name = params['name']
  auth = params['auth']

  expected_auth = Digest::MD5.hexdigest("#{@name}SECRET_SALT")
  @logged_in = (auth == expected_auth)

  songs = Dir.glob("public/music/*.mp3").map do |path|
    name = File.basename(path, ".mp3")
    {
      title: name.capitalize.gsub('_', ' '),
      audio: "/music/#{name}.mp3",
      image: "/images/#{name}.jpg"
    }
  end
  @playlist_json = songs.to_json
  erb :player
end

get '/donate' do
  erb :donate
end

__END__
