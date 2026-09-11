-- Rendering only: local math tags, readable source blocks and PDF line breaks.
function Math(el)
  if el.mathtype == 'DisplayMath' then
    el.text = el.text:gsub('\\begin{split}', '\\begin{aligned}'):gsub('\\end{split}', '\\end{aligned}')
    el.text = el.text:gsub('(\\tag%b{})(%s*\\end{aligned})', function(tag, ending) return ending .. tag end)
  end
  return el
end

function Code(el)
  -- Permit wraps inside table coefficient lists, file paths and long hashes.
  -- Break opportunities add no characters to the mathematical/source text.
  if #el.text > 10 then
    local chars = {}
    local escapes = {['\\']='\\textbackslash{}', ['^']='\\textasciicircum{}', ['~']='\\textasciitilde{}'}
    for i = 1, #el.text do
      local c = el.text:sub(i,i)
      local e = escapes[c] or (c:match('[%%#$&_{}]') and '\\' .. c or c)
      table.insert(chars,e)
      if c == ',' or c == '/' or c == '_' or (#el.text > 48 and i % 8 == 0) then
        table.insert(chars,'\\allowbreak{}')
      end
    end
    return pandoc.RawInline('latex', '\\texttt{' .. table.concat(chars) .. '}')
  end
end

function Table(el)
  if #el.colspecs == 7 then
    local widths = {0.16,0.18,0.05,0.05,0.23,0.24,0.09}
    for i,w in ipairs(widths) do el.colspecs[i][2]=w end
    return el
  end
end
