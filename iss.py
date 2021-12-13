<prog> -> requie "ifj21"<prog> 
<prog> -> global id : function (<global_param>) : <type> <prog>
<prog> -> function id (<param>) : <type> <orders> return <rt> end 
<prog> -> EOF
<type> -> ε
<type> -> <val><types>
<types> -> ε
<types> -> ,<val><types>
<param> -> id : <val> <params>
<param> -> ε
<params> -> ,id : <val> <params>
<params> -> ε
<rt> -> id <rts>
<rts> -> ,id <rts>
<rts> -> ε
<assignment> -> id <ids> = <exp><exps> <orders>
<global_param> -> <val><global_params>
<global_param> -> ε
<global_params> -> ,<val><global_param>
<global_params> -> ε
<orders> -> ε
<orders> -> local id : <type> = <exp> <call-fce> <orders>
<orders> -> <call-fce> <orders>
<orders> -> while <exp> do <orders> end <orders>
<orders> -> if <exp> then <orders> else <orders> end <orders>
<orders> -> <assignment>
<func_param> -> ε
<func_param> -> <val_f> <func_params> 
<func_params> -> ε
<func_params> -> , <vaL_f> <func_params> 
<call-fce> -> id (<func_param>)
<call-fce> -> ε
<ids> -> ,id <ids>
<ids> -> ε
<exps> -> ,<exp> <exps>
<exps> -> ε
<val> -> nil
<val> -> number
<val> -> integer
<val> -> string
<val_f> -> nil
<val_f> -> decimal_value
<val_f> -> float_value
<val_f> -> string_value
<val_f> -> ε