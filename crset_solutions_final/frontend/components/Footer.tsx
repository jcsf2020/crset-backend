export default function Footer() {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="col-span-1 md:col-span-2">
            <h3 className="text-2xl font-bold mb-4">CRSET Solutions</h3>
            <p className="text-gray-300 mb-4">
              Transformamos ideias em soluções tecnológicas inovadoras. 
              Especialistas em desenvolvimento web, automação e consultoria digital.
            </p>
            <div className="flex space-x-4">
              <a href="mailto:crsetsolutions@gmail.com" className="text-gray-300 hover:text-white transition-colors">
                Email
              </a>
              <a href="tel:+351914423688" className="text-gray-300 hover:text-white transition-colors">
                Telefone
              </a>
            </div>
          </div>
          
          <div>
            <h4 className="text-lg font-semibold mb-4">Serviços</h4>
            <ul className="space-y-2">
              <li><a href="#services" className="text-gray-300 hover:text-white transition-colors">Desenvolvimento Web</a></li>
              <li><a href="#services" className="text-gray-300 hover:text-white transition-colors">Automação</a></li>
              <li><a href="#services" className="text-gray-300 hover:text-white transition-colors">Consultoria</a></li>
            </ul>
          </div>
          
          <div>
            <h4 className="text-lg font-semibold mb-4">Empresa</h4>
            <ul className="space-y-2">
              <li><a href="#contact" className="text-gray-300 hover:text-white transition-colors">Contacto</a></li>
              <li><a href="/dashboard" className="text-gray-300 hover:text-white transition-colors">Dashboard</a></li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-800 mt-8 pt-8 text-center">
          <p className="text-gray-300">
            © 2025 CRSET Solutions. Todos os direitos reservados.
          </p>
        </div>
      </div>
    </footer>
  )
}
