#!/Users/perry/.rvm/rubies/ruby-3.1.0/bin/ruby

#!/usr/bin/ruby

#file = "d_dense_schedule.in.txt"#{ARGV[0] => 0}

files = Dir["input_data/*"]

def writeFile ret, file, score
  puts file
  File.open("../out/#{file.split("/").last}_#{score}.a", "w") { |out|
    out.write "#{ret.size}\n"
    out.write ret.join("\n")
  }
end



files.each do |file|

  numC, numP = nil
  contributors = []
  projects = []

  File.open(file, "r") { |input| 
  	rows = input.read.split("\n")

  	numC, numP = rows.shift.split.map &:to_i
  
    numC.times { # parse contributors
      name, numS = rows.shift.split
    
      contributorSkills = {}
    
      numS.to_i.times { # parse skills
        skillName, level = rows.shift.split
        contributorSkills[skillName] = level.to_i
      }
      contributors << {name:, skills: contributorSkills}
    }
  
    numP.times { # parse projects
      name, daysToComplete, score, bestBefore, numOfRoles = rows.shift.split
    
      requiredSkills = []
    
      numOfRoles.to_i.times { # parse required skills
        skillName, level = rows.shift.split
        requiredSkills << {name: skillName, level: level.to_i}
      }
    
      projects << {name:, daysToComplete: daysToComplete.to_f, score: score.to_f, bestBefore: bestBefore.to_i, requiredSkills:}
    }
   }
 
  output = []

  def findContributor skill, contributors, exclude
    i = contributors.index {|ce| !exclude[ce[:name]] && ce[:skills][skill[:name]] && ce[:skills][skill[:name]] >= skill[:level]}
    if i
      c = contributors.delete_at(i)
      contributors.push(c)
      exclude[c[:name]] = 1
      # for some reason this leveling isn't always accepted. Dunno why
      #c[:skills][skill[:name]] += 1 if c[:skills][skill[:name]] <= skill[:level]
      c[:name]
    end
  end

  projects.sort_by{|p| [p[:bestBefore],p[:score]*-1/p[:daysToComplete]]}.each do |p|
    alocatedContributors = {}
    alocations = p[:requiredSkills].map{ |s| findContributor(s, contributors, alocatedContributors) }.compact
    output << [p[:name], alocations.join(' ')].join("\n") if alocations.length == p[:requiredSkills].length
  end

  score = output.size

  writeFile(output, file, score)
end

#p projects

#p contributors