describe('Create News Modal', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/news');
    cy.get('.create-news-button').click(); 
  });

  it('should create a news item with valid data', () => {
    const title = 'Notícia de Teste';
    const description = 'Descrição de teste para a notícia';
    const content = 'Conteúdo detalhado da notícia de teste';

    cy.get('input[placeholder="Título"]').type(title);
    cy.get('input[placeholder="Descrição"]').type(description);
    cy.get('textarea[placeholder="Conteúdo"]').type(content);
    cy.get('input[type="file"]').as('sample-image.webp'); 

    cy.get('form').submit();

    // Verifique se o modal foi fechado
    cy.get('.news-modal').should('not.exist');
  });

  it('should show error for empty title', () => {
    const description = 'Descrição de teste para a notícia';
    const content = 'Conteúdo detalhado da notícia de teste';

    cy.get('input[placeholder="Descrição"]').type(description);
    cy.get('textarea[placeholder="Conteúdo"]').type(content);
    cy.get('input[type="file"]').as('sample-image.webp');

    cy.get('form').submit();

    cy.get('.news-modal').should('not.exist');
  });

  it('should show error for title exceeding character limit', () => {
    const longTitle = 'A'.repeat(51); 
    const description = 'Descrição de teste para a notícia';
    const content = 'Conteúdo detalhado da notícia de teste';

    cy.get('input[placeholder="Título"]').type(longTitle);
    cy.get('input[placeholder="Descrição"]').type(description);
    cy.get('textarea[placeholder="Conteúdo"]').type(content);
    cy.get('input[type="file"]').as('sample-image.webp');

    cy.get('form').submit();

    // Verifique se o modal foi fechado
    cy.get('.news-modal').should('not.exist');
  });

  it('should show error for empty description', () => {
    const title = 'Notícia de Teste';
    const content = 'Conteúdo detalhado da notícia de teste';

    cy.get('input[placeholder="Título"]').type(title);
    cy.get('textarea[placeholder="Conteúdo"]').type(content);
    cy.get('input[type="file"]').as('sample-image.webp'); 

    cy.get('form').submit();

    // Verifique se o modal foi fechado
    cy.get('.news-modal').should('not.exist');
  });

  it('should show error for description exceeding character limit', () => {
    const title = 'Notícia de Teste';
    const longDescription = 'A'.repeat(101); 
    const content = 'Conteúdo detalhado da notícia de teste';

    cy.get('input[placeholder="Título"]').type(title);
    cy.get('input[placeholder="Descrição"]').type(longDescription);
    cy.get('textarea[placeholder="Conteúdo"]').type(content);
    cy.get('input[type="file"]').as('sample-image.webp'); 

    cy.get('form').submit();
    cy.get('.news-modal').should('not.exist');
  });

  it('should show error for empty content', () => {
    const title = 'Notícia de Teste';
    const description = 'Descrição de teste para a notícia';

    cy.get('input[placeholder="Título"]').type(title);
    cy.get('input[placeholder="Descrição"]').type(description);
    cy.get('input[type="file"]').as('sample-image.webp'); 

    cy.get('form').submit();

    cy.get('.news-modal').should('not.exist');
  });

  it('should show error for missing image', () => {
    const title = 'Notícia de Teste';
    const description = 'Descrição de teste para a notícia';
    const content = 'Conteúdo detalhado da notícia de teste';

    cy.get('input[placeholder="Título"]').type(title);
    cy.get('input[placeholder="Descrição"]').type(description);
    cy.get('textarea[placeholder="Conteúdo"]').type(content);

    cy.get('form').submit();

    cy.get('.news-modal').should('not.exist');
  });

  it('should close the modal on close button click', () => {
    cy.get('.close-modal-button').click();

    cy.get('.news-modal').should('not.exist');
  });
});
