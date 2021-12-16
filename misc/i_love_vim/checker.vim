function! GetCol(n, pos) abort
	let n = a:n
	let col = ""
	while n !=# 0
		let col = col . getline('.')[a:pos]
		normal j
		let n = n - 1
	endwhile

	execute "normal " . repeat("k", a:n)
	return col
endfunction
	

function! Check() abort
	let col_regexes = ['F[SLNGY]\([!@#\$_]\)*[ORCH]\1[TIMELIMIT]*', 'L.[VERY][STAN][amoGUs][RESTAPI]*[OKAY]', 'A[URGI]*[RUST][^\d!.,:;][SAST].[N...]', 'G[^\dA-Za-z][MARGARET][EBOI]_[NONCE][TRCK][GREY]', '{[LO_ST]*N\w[DEDOUTSIDE]\w[ASYNC]', 'N\d\([TRATATA]\)*\(\d\)\2[248]\1', '\(OVO\|EGG\|DAG\)\([_\-?]\)\([NM]\)\3\2[ES]', '[WSX][EXEC]\(OY\|AY\)\([E3]\)\w\2}']
	let row_regexes = ['FLAG{[ABCDQNO5]*[QWER]', '[YUIO]O[UJNBY_]\{1,2}[HAL0]*[VARARGS][EVAL]', '[_\/<>,.][VIM_]*[2CHUTO]\{1,3}', '[-_\/\\][AREWDK]\{1,3}[NT]*_[YOUSHALLN0TP4SS]\+', '[OUISEMPAI]\+[?!.,:;]_\(S0ME\|4NY\|N0N3\)[\d_]*', '\([_";&*]\)[RL][NDA]*[0M]*\1', '\([VSTA]\)\([HELLO]\)X\1\([_ABC?]\)[123]\3\2', '[DUNO]*[LVA][ONOFF]\+[GOD][ARMX86][TERM]*}']
	let n = 8

	let i = 0
	while i !=# n
		let str = getline('.')
		if str !~# row_regexes[i]
			echom "Failed"
			return 0
		endif
		normal j
		let i = i + 1
	endwhile

	execute "normal " . repeat("k", n)

	let i = 0
	
	while i !=# n
		let str = GetCol(n, i)
		if str !~? col_regexes[i]
			echom "Failed"
			return 0
		endif
		let i = i + 1
	endwhile
	
	echom "SUCCESS"
	return 1
endfunction
