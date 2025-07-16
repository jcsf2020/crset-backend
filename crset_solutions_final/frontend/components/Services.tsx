'use client'

import { useEffect, useState } from 'react'
import axios from 'axios'

interface Service {
  id: number
  title: string
  description: string
  price: number
  category: string
}

export default function Services() {
  const [services, setServices] = useState<Service[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchServices()
  }, [])

  const fetchServices = async () => {
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/services/`)
      setServices(response.data)
    } catch (error) {
      console.error('Error fetching services:', error)
      // Fallback services for demo
      setServices([
        {
          id: 1,
          title: 'Desenvolvimento Web',
          description: 'Sites e aplicações web modernas e responsivas',
          price: 999,
          category: 'Desenvolvimento'
        },
        {
          id: 2,
          title: 'Automação de Processos',
          description: 'Automatização de tarefas e workflows empresariais',
          price: 1499,
          category: 'Automação'
        },
        {
          id: 3,
          title: 'Consultoria Tecnológica',
          description: 'Consultoria estratégica em tecnologia e transformação digital',
          price: 199,
          category: 'Consultoria'
        }
      ])
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <section id="services" className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="animate-pulse">
              <div className="h-8 bg-gray-300 rounded w-64 mx-auto mb-4"></div>
              <div className="h-4 bg-gray-300 rounded w-96 mx-auto"></div>
            </div>
          </div>
        </div>
      </section>
    )
  }

  return (
    <section id="services" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Os Nossos Serviços
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Oferecemos soluções completas para transformar o teu negócio digitalmente
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service) => (
            <div key={service.id} className="bg-gray-50 rounded-lg p-8 hover:shadow-lg transition-shadow">
              <div className="mb-4">
                <span className="inline-block bg-primary-100 text-primary-600 text-sm font-medium px-3 py-1 rounded-full">
                  {service.category}
                </span>
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">
                {service.title}
              </h3>
              <p className="text-gray-600 mb-6">
                {service.description}
              </p>
              <div className="flex items-center justify-between">
                <span className="text-2xl font-bold text-primary-600">
                  €{service.price}
                </span>
                <a href="#contact" className="btn-primary">
                  Saber Mais
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
