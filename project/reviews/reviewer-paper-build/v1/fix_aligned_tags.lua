-- Editorial Pandoc filter for reviewer PDFs.
--
-- Some canonical Markdown proofs put \tag{...} at the end of the final line
-- inside an amsmath `aligned` environment. Markdown renderers accept this
-- presentation, but amsmath requires the tag to belong to the enclosing display.
-- Move only that tag across \end{aligned}; mathematical content and numbering
-- are unchanged, and the canonical proof source is not edited.

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
