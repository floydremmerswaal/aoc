file_data = File.readlines("input.txt").map(&:chomp).join(" ")

def parse_line_part1(line)
    regex = /mul\((\d+),(\d+)\)/

    matches = line.scan(regex)

    sum = 0
    
    matches.each do |match|
        sum += match[0].to_i * match[1].to_i
    end
    return sum
end

def parse_line_part2(line)
    regex = /mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))/

    matches = line.scan(regex)

    sum = 0
    to_do = true

    for i in 0..matches.length-1
        match = matches[i]
        if match[2] == "do()"
            to_do = true
        elsif match[3] == "don't()"
            to_do = false
        else
            if to_do
                sum += match[0].to_i * match[1].to_i
            end
        end
    end
    return sum
end

sum = parse_line_part1(file_data)
puts "Part 1: #{sum}"

sum = parse_line_part2(file_data)
puts "Part 2: #{sum}"