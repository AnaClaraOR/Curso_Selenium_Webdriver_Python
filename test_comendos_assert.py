## O assert sempre verifica se o retorno da condição é true
assert True

## assert numbers
# num_esperado = 1
# num_obtido = 2
# assert num_esperado == num_obtido, f"Esperado {num_esperado}. Atual {num_obtido}."

#pode ser utilizado qualquer tipo de condicional (maior, menor, diferente...)
# assert num_esperado > num_obtido, f"Esperado {num_esperado}. Atual {num_obtido}."

## assert text
# text_esperado = "Selenium Webdriver"
# text_obtido = "Selenium webdriver"
# assert text_esperado == text_obtido, f"Esperado {text_esperado}. Atual {text_obtido}."

#diminui o texto para não ser case sensitive, ficando todos minusculos
#assert text_esperado.lower() == text_obtido.lower(), f"Esperado {text_esperado}. Atual {text_obtido}."

## assert text in string
text_esperado = "Seleniummmmmmmmmmmmmm"
text_obtido = "Selenium webdriver"
assert text_esperado in text_obtido, f"Esperado '{text_esperado}' dentro da string atual '{text_obtido}'."

# assert text_esperado not in text_obtido, f"Esperado '{text_esperado}' dentro da string atual '{text_obtido}'."

## assert is_displayed/is_enabled/is_selected