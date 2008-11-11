o = $db.data.findOne()

puts '<html><body>'
puts 'Hello from Ruby!<br/>'

unless o
    puts 'This is the first visit'
    o = { 'lang'=> 'Ruby', 'date'=> Time.new.to_s, 'count'=> 1 }
else
    puts "Last visit was visit #{o['count']} from language #{o['lang']} on #{o['date']}" 
    o['count'] = o['count'] + 1
    o['lang'] = 'Ruby'
    o['date'] = Time.new.to_s
end

$db.data.save(o)

puts '<br/>'
puts "<a href='/javascript'>JavaScript</a> &nbsp <a href='/python'>Python</a> &nbsp; <a href='/ruby'>Ruby</a>"

puts '</body></html>'


