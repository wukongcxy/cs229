__author__ = 'chenxinyue'
import numpy


def lms(x_data, y_data, alpha, theta, train_times):
    next_theta = theta
    for i in range(0, train_times):
        next_theta = train(x_data, y_data, alpha, next_theta)
        print str(i) + "/" + str(train_times)
        print next_theta
        print j(x_data, y_data, next_theta)
    return next_theta


def train(x_data, y_data, alpha, theta):
    delta = []
    errors = []
    for i in range(0, len(y_data)):
        h = numpy.dot(x_data[i], theta)
        error = y_data[i] - h
        errors.append(error)
    errors = numpy.array(errors)
    for i in range(0, len(theta)):
        delta.append(alpha * numpy.dot(errors, x_data[:, i]))
    return theta + delta


def j(x_data, y_data, theta):
    delta = numpy.dot(x_data, theta) - y_data
    return 0.5 * numpy.dot(delta, delta)

if __name__ == '__main__':
    x_data = numpy.array([[1] + [x + 5] for x in range(0, 46)])
    y_data = numpy.array([4.593246315825569, 5.7035581857882622, 7.2055959985285112, 7.8993521738471211, 9.345075607960684, 9.7969299365739264, 11.147945534358318, 11.994184854742285, 13.039084626355979, 14.140130262853813, 14.574630461355863, 16.344239451526597, 17.234467216037363, 18.312816192113086, 19.055217114621062, 20.085523639142025, 20.811804429692891, 22.305382305982903, 23.491987977375388, 23.536500553575859, 25.335358515978527, 26.052097656789208, 27.441973233529705, 27.987039796893754, 28.520456928455609, 29.597980985159722, 31.370183277009254, 31.889342337174703, 33.264350969160112, 34.166611412102917, 34.560168919793163, 36.439466150192018, 37.000826727456996, 38.135237182512938, 39.11402177951944, 39.554117653264136, 40.690978306077675, 42.40918686077503, 43.324774989906842, 43.840555522955206, 45.110740037330224, 46.349346433082154, 46.861768977380343, 48.494025968979884, 49.062560108966558, 49.908448071513561])
    #x_data = numpy.array([[1] + [x] for x in range(5, 17)])
    #y_data = numpy.array([4.593246315825569, 5.7035581857882622, 7.2055959985285112, 7.8993521738471211, 9.345075607960684, 9.7969299365739264, 11.147945534358318, 11.994184854742285, 13.039084626355979, 14.140130262853813, 14.574630461355863, 16.344239451526597])
    alpha = 0.00001
    theta = theta = numpy.array([0, 2])

    train_times = 100000
    last_theta = lms(x_data, y_data, alpha, theta, train_times)
    print last_theta
