local warning_patterns = {
  "Intel.*MKL.*WARNING",
}

function CodeBlock(el)
  local contains_warning = false
  for _, pattern in ipairs(warning_patterns) do
    if el.text:find(pattern) then
      contains_warning = true
      break
    end
  end

  if not contains_warning then
    return el
  end

  local filtered_lines = {}
  for line in (el.text .. "\n"):gmatch("([^\n]*)\n") do
    local should_keep = true
    for _, pattern in ipairs(warning_patterns) do
      if line:find(pattern) then
        should_keep = false
        break
      end
    end
    if should_keep then
      table.insert(filtered_lines, line)
    end
  end

  el.text = table.concat(filtered_lines, "\n")
  return el
end
