-- Editorial Pandoc filter for reviewer PDFs.
--
-- 1. Some canonical Markdown proofs put \tag{...} at the end of the final line
--    inside an amsmath `aligned` environment. Markdown renderers accept this
--    presentation, but amsmath requires the tag to belong to the enclosing display.
--    Move only that tag across \end{aligned}; mathematical content and numbering
--    are unchanged, and the canonical proof source is not edited.
-- 2. One audit note writes the set difference in prose as B=V(H)\N_H[v]. With
--    raw TeX enabled Pandoc isolates \N as a RawInline and XeLaTeX treats it as an
--    undefined command. Render that exact raw token as the Unicode set-difference
--    sign. This is an editorial rendering fix only; the audit source is untouched.

function Math(el)
  if el.mathtype ~= 'DisplayMath' then
    return nil
  end
  local fixed, n = el.text:gsub('(\\tag%b{})(%s*\\end{aligned})', function(tag, ending)
    return ending .. tag
  end)
  if n > 0 then
    el.text = fixed
    return el
  end
  return nil
end

function RawInline(el)
  if el.format == 'tex' and el.text == '\\N' then
    return pandoc.Str('∖N')
  end
  return nil
end
