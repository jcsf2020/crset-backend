'use client'

import { useState } from 'react'
import axios from 'axios'

export default function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    message: ''
  })
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/contacts/`, formData)
      setSuccess(true)
      setFormData({ name: '', email: '', phone: '', message: '' })
    } catch (err) {
      setError('Erro ao enviar mensagem. Tenta novamente.')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  if (success) {
    return (
      <section id="contact" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-2xl mx-auto text-center">
            <div className="bg-green-50 border border-green-200 rounded-lg p-8">
              <div className="text-green-600 text-6xl mb-4">✓</div>
              <h3 className="text-2xl font-bold text-green-800 mb-2">Mensagem Enviada!</h3>
              <p className="text-green-700 mb-6">
                Obrigado pelo teu contacto. Responderemos em breve.
              </p>
              <button 
                onClick={() => setSuccess(false)}
                className="btn-primary"
              >
                Enviar Nova Mensagem
              </button>
            </div>
          </div>
        </div>
      </section>
    )
  }

  return (
    <section id="contact" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Vamos Conversar
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Tens um projeto em mente? Entra em contacto connosco e vamos transformar a tua ideia em realidade.
          </p>
        </div>

        <div className="max-w-2xl mx-auto">
          <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-lg p-8">
            {error && (
              <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-6">
                {error}
              </div>
            )}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-2">
                  Nome *
                </label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  required
                  value={formData.name}
                  onChange={handleChange}
                  className="input-field"
                  placeholder="O teu nome"
                />
              </div>
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                  Email *
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                  className="input-field"
                  placeholder="teu@email.com"
                />
              </div>
            </div>

            <div className="mb-6">
              <label htmlFor="phone" className="block text-sm font-medium text-gray-700 mb-2">
                Telefone
              </label>
              <input
                type="tel"
                id="phone"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                className="input-field"
                placeholder="+351 912 345 678"
              />
            </div>

            <div className="mb-6">
              <label htmlFor="message" className="block text-sm font-medium text-gray-700 mb-2">
                Mensagem *
              </label>
              <textarea
                id="message"
                name="message"
                required
                rows={5}
                value={formData.message}
                onChange={handleChange}
                className="input-field resize-none"
                placeholder="Conta-nos sobre o teu projeto..."
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'A enviar...' : 'Enviar Mensagem'}
            </button>
          </form>

          <div className="mt-12 text-center">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div>
                <h4 className="font-bold text-gray-900 mb-2">Email</h4>
                <p className="text-gray-600">crsetsolutions@gmail.com</p>
              </div>
              <div>
                <h4 className="font-bold text-gray-900 mb-2">Telefone</h4>
                <p className="text-gray-600">+351 914 423 688</p>
              </div>
              <div>
                <h4 className="font-bold text-gray-900 mb-2">Localização</h4>
                <p className="text-gray-600">Vila Nova de Gaia, Portugal</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
