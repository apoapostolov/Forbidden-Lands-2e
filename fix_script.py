path = '/home/apoapostolov/git-public/Forbidden-Lands-2e/02-gamemasters-guide/07-artifacts.md'
with open(path, 'r') as f:
    content = f.read()

# Fix 1: Remove bare ### before ### Appearance in Arrows of the Fire Wyrm
idx = content.find('_\n###\n### Appearance\n')
if idx != -1:
    old = content[idx:idx+len('_\n###\n### Appearance\n')]
    new = '_\n### Appearance\n'
    content = content.replace(old, new, 1)
    print('Fix 1: OK')
else:
    print('Fix 1: NOT FOUND')

# Fix 2: Nightwalker's Hourglass — rejoin legend, move Pelagia line after legend as ### Suggested Location
old2 = content.find('The only answer to Dordela\'s questions was a hiss:_\n\nPelagia (see _Raven\'s Purge_ ).\n\n> _"Fracture time')
if old2 != -1:
    # Extract exact strings using slicing
    a = content[old2:]
    # old block ends after the second blockquote block (Only one hourglass now remains in the box.)
    # We need to rejoin the legend: remove the Pelagia line from mid-legend and add ### Suggested Location section after legend ends
    # The structure we want:
    # ...was a hiss: "Fracture time, unmake mistake, bone break," and then..._
    # (rest of blockquote)
    # ...Only one hourglass now remains in the box.
    #
    # ### Suggested Location
    # Pelagia (see _Raven's Purge_ ).
    #
    # ### Appearance
    
    old_block = 'The only answer to Dordela\'s questions was a hiss:_\n\nPelagia (see _Raven\'s Purge_ ).\n\n> _"Fracture time, unmake mistake, bone break," and then the mysterious messenger was gone.'
    new_block = 'The only answer to Dordela\'s questions was a hiss: \u201cFracture time, unmake mistake, bone break,\u201d and then the mysterious messenger was gone.'
    # Check if old_block exists verbatim
    if old_block in content:
        content = content.replace(old_block, new_block, 1)
        print('Fix 2a: OK')
    else:
        # Try without smart quotes
        old_block2 = 'The only answer to Dordela\'s questions was a hiss:_\n\nPelagia (see _Raven\'s Purge_ ).\n\n> _"Fracture time, unmake mistake, bone break," and then the mysterious messenger was gone.'
        idx2 = content.find('The only answer to Dordela')
        end2 = content.find('mysterious messenger was gone.', idx2) + len('mysterious messenger was gone.')
        actual_old = content[idx2:end2]
        print('Fix 2a actual old:', repr(actual_old))
        print('Fix 2a: NOT FOUND')
else:
    # Try finding just the Pelagia line position
    idx_p = content.find('\nPelagia (see _Raven\'s Purge_ ).\n\n> _"Fracture time')
    if idx_p != -1:
        end_p = idx_p + len('\nPelagia (see _Raven\'s Purge_ ).\n\n> _"Fracture time')
        print('Fix 2 partial found at', idx_p, ':', repr(content[idx_p-50:idx_p+80]))
    print('Fix 2: NOT FOUND')

with open(path, 'w') as f:
    f.write(content)
print('Written.')
