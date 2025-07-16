export default function Hero() {
  return (
    <section className="bg-gradient-to-r from-primary-600 to-primary-700 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <div className="text-center">
          <h1 className="text-4xl md:text-6xl font-bold mb-6">
            Soluções Tecnológicas
            <span className="block text-primary-200">Sob Medida</span>
          </h1>
          <p className="text-xl md:text-2xl mb-8 text-primary-100 max-w-3xl mx-auto">
            Transformamos as tuas ideias em realidade digital. 
            Desenvolvimento web, automação e consultoria tecnológica para o teu negócio.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="#contact" className="bg-white text-primary-600 hover:bg-gray-100 font-bold py-3 px-8 rounded-lg transition-colors">
              Começar Projeto
            </a>
            <a href="#services" className="border-2 border-white text-white hover:bg-white hover:text-primary-600 font-bold py-3 px-8 rounded-lg transition-colors">
              Ver Serviços
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
